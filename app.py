from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

FAQ = {
    "what is your name": "I am FAQBot 🤖",
    "how are you": "I am doing great, thanks for asking!",
    "what is python": "Python is high-level,interpreted programming language.",
    "who created you": "I was created by a Python developer just like you!",
    "bye": "Goodbye! Have a nice day 😊"
}


def reply_to(user_text: str) -> str:
    text = user_text.lower().strip()
    text = re.sub(r"[^\w\s]", "", text)
    if text in FAQ:
        return FAQ[text]
    # simple fuzzy-ish match: return first key contained in text
    for k, v in FAQ.items():
        if k in text:
            return v
    return "Sorry, I don’t know that. Try another question."


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    user = data.get("message", "")
    return jsonify({"reply": reply_to(user)})


if __name__ == "__main__":
    app.run(debug=True)
