'''Given an integer n. Write a program to find the nth Fibonacci number.

F(0)= 0, F(1)=1
The nth Fibonacci number is given by the forumla F(n) = F(n-1) + F(n-2). The first few fibonacci numbers are: 0 1 1 2 3 5. . . . '''

n = int(input("Enter a number (0-10):"))
if n == 0 :
    print(0)
elif n == 1 :
    print(1)#0+1
elif n == 2 :
    print(1)#0+1
elif n == 3 :
    print(2)#1+1
elif n == 4 :
    print(3)#1+2
elif n == 5 :
    print(5)#3+2
elif n == 6 :
    print(8)#5+3
elif n == 7 :
    print(13)#8+5
elif n == 8 :
    print(21)#8+13
elif n == 9 :
    print(34)#21+13
elif n == 10 :
    print(55)#34+21
else:
    print("This program prints only from 1-10 conditions")


'''Given an integer n check if n is prime or not.
A prime number is a number that is divisible by 1 and itself only.

Note: Print "True" if n is prime, otherwise print "False".'''

n = int(input("Enter a Number n:"))
if n % 1 == 1:
    print("n is a Prime Number")
