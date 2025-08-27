# lists: list are nothing but a variable used to store multiple valuse
# There are 4 built in data types in python.
# lists, tuple , dictionaries and set.
# Lists are creted using square backets [].
# example down
thislist = ["apple", "banana", "cherry"]
print(thislist)

# There are four collection data types in the Python programming language:
# List is a collection which is ordered and changeable.
# Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable
# Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed.
# No duplicate members.
# Dictionary is a collection which is ordered** and changeable.
# No duplicate members.

# The lists meathods are built-in functions to perform various operations
# in the list.

# List Methods :
# Let's look at different list methods in Python:
# append(): Adds an element to the end of the list.
# copy(): Returns a shallow copy of the list.
# clear(): Removes all elements from the list.
# count(): Returns the number of times a specified element appears in the list.
# extend(): Adds elements from another list to the end of the current list.
# index(): Returns the index of the first occurrence of a specified element.
# insert(): Inserts an element at a specified position.
# pop(): Removes and returns the element at the specified position
# remove(): Removes the first occurrence of a specified element.
# reverse(): It Reverses the order of the elements in the list.
# sort(): Sorts the list in ascending order (by default).

# Reverse programm syntax.
Numbers = [20, 30, 40, 50, 60]
Numbers.reverse()
print(Numbers)

marks = [25, 30, 35, 25, 40, 45, 25, 25, 25]
print(marks.count(25))

# Here with the help of copy syntax we are making a copy of Orignal.
original = ["Pineapple", "Apple", "banana"]
copy_list = original.copy()
copy_list.append("watermelon")

print(original)
print(copy_list)

# here we find the index of the alloted number.
nums = [100, 200, 300, 400, 500, 600, 700]
print(nums.index(300))

# Here we are arranging all the numbers in ascending and descending order,
# we use .sort() syntax.
score = [75, 80, 70, 72, 65]

score.sort()
print(score)
score.sort(reverse=True)
print(score)

fruits = ["apple", 'banana', "pineapple", "grapes"]

print(fruits.pop(1))
