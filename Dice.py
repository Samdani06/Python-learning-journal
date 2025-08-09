# You are given a cubic dice with 6 faces.
# All the individual faces have a  number printed on them.
# The numbers are in the range of 1 to 6, like any ordinary dice.
# You will be provided with a face of this cube,
# your task is to guess the  number on the opposite face of the cube.

"""Start
Input the number N (face number of the dice)
If N equals 1, then:
Print 6
Else if N equals 2, then:
Print 5
Else if N equals 3, then:
Print 4
Else if N equals 4, then:
Print 3
Else if N equals 5, then:
Print 2
Else if N equals 6, then:
Print 1
Else:
Print "Invalid input"
End"""


N = int(input("Enter the number on the Dice:"))
if N == 1:
    print(6)
elif N == 2:
    print(5)
elif N == 3:
    print(4)
elif N == 4:
    print(3)
elif N == 5:
    print(2)
elif N == 6:
    print(1)
else:
    print("Invalid input!")
