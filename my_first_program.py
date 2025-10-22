# We need to get an input from the user.
# Ensure that the input is a number.
# Count upto the number given by the user.
# Check if the counted number is greater than 5.
# If it's more, print.

user_input = input("Enter a number: ")

try:
    user_integer = int(user_input)
except ValueError:
    user_integer = 0
    print("That's not an int!")

for i in range(user_integer + 1):
    if i > 5:
        print(i)