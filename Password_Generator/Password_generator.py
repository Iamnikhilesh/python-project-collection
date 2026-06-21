import random

# Define character sets
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbol = "[]{}()/*-+;:?.,<>-_!@#$%^&`~"

# Combine all character sets
all = lower + upper + numbers + symbol

# Ask the user for the password length
try:
    length = int(input("What length of password do you need? "))
    if length > len(all):
        print(f"Password length cannot exceed {len(all)}, as it uses unique characters.")
    elif length <= 0:
        print("Password length must be greater than 0.")
    else:
        # Generate the password
        password = "".join(random.sample(all, length))
        print(f"Your password is: {password}")
except ValueError:
    print("Please enter a valid number.")
