'''If the number is divisible by 3, you print "Fizz" (without quotes)
If the number is divisible by 5, you print "Buzz" (without quotes)
If the number is divisible by both 3 and 5, you print "FizzBuzz" (without quotes)
In any other case, you print the number itself'''
    
number = int(input("Enter a number: ")) #here we input a number to find weather it is divisible by 3 or 5.

if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")   # Here if the number is divisible by both 3 and 5 then the output will be FizzBuzz.
elif number % 3 == 0:
    print("Fizz")   # Here if the number is divisible by 3 then the output will be Fizz.
elif number % 5 == 0:
    print("Buzz") # here of the number is divisible by 5 then the output will be Buzz.
else:
    print(number)

''' Given three numbers a, b, and c. You need to find which is the greatest of them all.'''

a = float(input("Enter Number (a):"))
b = float(input("Enter Number (b): "))
c = float(input("Enter Number (c): "))

# Check which one is the greatest using only conditional statements

if a >= b and a >= c:
    print("The greatest number is:", a)
elif b >= a and b >= c:
    print("The greatest number is:", b)
else:
    print("The greatest number is:", c )

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
