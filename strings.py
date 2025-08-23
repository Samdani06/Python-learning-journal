# In Python, a string is a sequence of characters, such as letters,
# numbers, or symbols, enclosed within single quotes (' '),
# double quotes (" "), or triple quotes (''' ''' or """ """).

# A = "Apple"
# b = 'Badmintion'
# whatever is written in the double quotes or single quotes it is a string.
# String meathods : These are nothing but small string functions which help
# in the string format.Here are a few string meathods.
# Lower() = This lower cases all the alphabets in the string.
# Upper() = This upper cases all the alphabets in the string.
# Strip() = This gives the trimmed version of the alphabet.
# Count() = Returns the number of times a specified value is there.
a = "Mathematics"
count = 0

for char in a:
    count += 1
print(count)

# enumerate(): Enumerare() function keeps the track of both index and value of
# the Elements within that iterable.
d = "Samdani"
s = 0

for i, a in enumerate(d):
    count += 1
print(d)
