"""You are given a number n. The number n can be negative or positive.
If n is negative, print numbers from n to 0
by adding 1 to n in the neg function.
If positive, print numbers from n-1 to 0
by subtracting 1 from n in the pos function.
Note:- You don't have to return anything, you just have to print the array.
Example 1:
Input:
n = 0
Output:
already Zero"""
N = int(input("Enter your Number: "))


def neg(n):
    for i in range(n, 1):
        print(i, end=' ')


def pos(n):
    for i in range(n - 1, -1, -1):
        print(i, end=' ')


if N == 0:
    print("Already zero")
elif N > 0:
    pos(N)
else:
    for i in range(N, 1):
        print(i, end=' ')
