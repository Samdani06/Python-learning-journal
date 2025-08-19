# Input: two numbers
# Here is a code for mini calculator.
a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))

# Input: operator code (1:add, 2:subtract, 3:multiply)
operator = int(input("Enter the operator (1:Add, 2:Subtract, 3:Multiply): "))

# Conditional logic
if operator == 1:
    result = a + b
    print("Result:", result)
elif operator == 2:
    result = a - b
    print("Result:", result)
elif operator == 3:
    result = a * b
    print("Result:", result)
else:
    print("Invalid Input")
