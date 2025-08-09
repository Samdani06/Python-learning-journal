# Given a number n, check if the number is perfect or not.
#  A number is said to be perfect if sum of all its
#  factors excluding the number itself is equal to the number.

n = int(input("Enter Your Number:"))
sum = 0
i = 1
while i < n:
    if n % i == 0:
        sum = sum + i
    i = i + 1
if sum == n:
    print("The number is Perfect!1")
else:
    print("Number is not perfect!!")
