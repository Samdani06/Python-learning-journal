# File Handling :-
# File handling refers to the process of performing operations on a file,
# such as creating, opening, reading, writing and closing it
# through a programming interface.

# Uses of File Handlimg :-
# To store data permanently, even after the program ends.
# To access external files like .txt, .csv, .json, etc.
# To process large files efficiently without using much memory.
# To automate tasks like reading configs or saving outputs.
# To handle input/output in real-world applications and tools.

# Here is how we open a file :
f = open("geek.txt", "w")
print(f)

# Here is how we close a file :
file = open("geek.txt", "r")
file.close()

open("file.txt", "x")
