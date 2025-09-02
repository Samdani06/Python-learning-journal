const chat = document.getElementById("chat");
const form = document.getElementById("composer");
const input = document.getElementById("message");

function addBubble(text, who = "bot") {
  const wrap = document.createElement("div");
  wrap.className = `msg ${who}`;
  const bubble = document.createElement("div");
  bubble.className = "bubble";
  bubble.textContent = text;
  wrap.appendChild(bubble);
  chat.appendChild(wrap);
  chat.scrollTop = chat.scrollHeight;
}

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  const text = input.value.trim();
  if (!text) return;
  addBubble(text, "user");
  input.value = "";

  // show a tiny typing indicator
  const typing = document.createElement("div");
  typing.className = "msg bot";
  typing.innerHTML = `<div class="bubble">...</div>`;
  chat.appendChild(typing);
  chat.scrollTop = chat.scrollHeight;

  try {
    const res = await fetch("/chat", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({ message: text })
    });
    const data = await res.json();
    typing.remove();
    addBubble(data.reply, "bot");
  } catch (err) {
    typing.remove();
    addBubble("Network error. Please try again.", "bot");
  }
});
