# I will take an input from the user.
user_input = input("Please enter a character: ")
# Then I will define the digits from 0 to 9.
digits = "0123456789"
# If the user input is a digit, I will print "You entered a digit."
for u_input in user_input:
    if u_input in digits:
        print("You entered a number.")
        user_input = int(user_input)
    # Otherwise, I will print "You did not enter a digit."
    else:
        print("You did not enter a number.")

# Now I will check if the user input is an integer.
if (type(user_input) is int):
    # I will check if the integer is greater than, equal to, or less than 5.
    if (user_input > 5):
        print("The number is greater than 5.")
    elif user_input == 5:
        print("The number is equal to 5.")
    else:
        print("The number is less than 5.")