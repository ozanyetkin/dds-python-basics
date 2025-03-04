"""
I will program a simple script
that will ask a number to the user
and then it will multiply it by 10
and then it will give the result
"""

my_multiplier = 10

user_number = input("Please, give me a number: ")

# I need to check whether the user input is a number
digits = "0123456789"

# Change the condition to make it work for valid numbers
if user_number:
    print(user_number * my_multiplier)
else:
    print("You did not give me a number. Please, try again.")
