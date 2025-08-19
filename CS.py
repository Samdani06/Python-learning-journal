# Conditional statements : CS in python execute
# a block of code if the specific conditions are met.
# An "if statement" is written by using the 'if' keyword.

a = 80
b = 55
if a > b:
    print("a is greater than b")

# The elif keyword is Python's way of saying "if the previous conditions
# were not true, then continue the other condition".

a = 20
b = 20
if a > b:
    print("a is greater than b")
elif a == b:
    print("a is Equal to b")


# The Else keyword catches anything which isn't
# caught by the previous condition.

a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")
# Here the conditions didnt meet with if neither elif so else condition
# catches the previous condition.

# You can have if statements inside if statements,
# this is called nested if statements.
x = 45

"""if x > 10:
    print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")"""
