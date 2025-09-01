# When an error occurs, or exception as we call it, Python will
# normally stop and generate an error message.
# These exceptions can be handled using the try statement:
try:
    print(x)
except:
    print("An exception occurred")
# The try block lets you test a block of code for errors.

# The except block lets you handle the error.

# The finally block lets you execute code,
# regardless of the result of the try- and except blocks.

# Exceptional handling :
# Python Exception Handling handles errors
# that occur during the execution of a program.
# Exception handling allows to respond to the error,
# instead of crashing the running program.
# It enables you to catch and manage errors,
# making your code more robust and user-friendly.
n = 0
try :
    res = n / 0
except ZeroDivisionError:
    print("Cant be devided ny Zero")