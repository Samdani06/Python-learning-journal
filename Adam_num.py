# Today I practice few Quetions in conditional statements.
# Through practcing these quetions i can upgrade my Algorithm solving skills
# and Learn more about conditional statements.


def reverse_number(num):

# Here we are reversing the number that we give as
# input to check weather the given num is reversible or not.
    return int(str(num)[::-1])


def is_adam_number(N):
    R = reverse_number(N)  # Here we reverse the number N to Get R.
    N_squared = N * N
    R_squared = R * R

    revN_squared = reverse_number(N_squared)
    revR_squared = reverse_number(R_squared)

    if revN_squared == revR_squared and revR_squared == revN_squared:
        print(f"{N} is an Adam Number!")
    else:
        print(f"{N} is not an Adam Number ")


N = int(input("Enter an number:"))
is_adam_number


def reverse_number(num):
    """Reverses the digits of the given number."""
    return int(str(num)[::-1])


def is_adam_number(N):
    """Checks if the number is an Adam number."""

# Step 1: Reverse N to get R
    R = reverse_number(N)

    # Step 2: Compute N^2 and R^2
    N_squared = N * N
    R_squared = R * R

    # Step 3: Reverse N^2
    revN_squared = reverse_number(N_squared)

    # Step 4: Check if reverse of N^2 equals R^2
    if revN_squared == R_squared:
        print(f"{N} is an Adam number")
    else:
        print(f"{N} is not an Adam number")

# Input from user


N = int(input("Enter a number: "))
is_adam_number(N)
