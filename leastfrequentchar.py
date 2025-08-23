# This is a least frequent character counter this counts all the aplhabets and
# tells the least number of alphabet present.

from collections import Counter
s = "nuemonoultrafaguesdiseas"
freq = Counter(s)
res = min(freq, key=freq.get)
print(str(res))

s = "Hello,World!"
frequency = Counter(s)
max_char = max(frequency, key=frequency.get)

print(max_char)
