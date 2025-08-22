# First we Take input from the user
N = int(input("Enter a number to print its multiplication table: "))

# Now we write the multiplication table from 1 to 10.
for i in range(1, 11):
    result = N * i
    print(f"{N} x {i} = {result}")

"""You are given a string s, you need to print its characters at
even indices(index starts at 0).
Note: Please go through the range function to understand how to jump 2 steps.
Examples:
Input: s = "DoctorPhenomenal"
Output: DcoPeoea"""

"""s = input("Enter a string: ")  # here we input the string.

# Loop through each character using its index
for i in range(len(s)):
    if i % 2 == 0:
        print(s[i], end='')"""
