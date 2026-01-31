# User Input Demonstration

print("=== User Input Collection ===")
print()

# Collecting string input
print("Let's collect some information about you!")
user_name = input("Please enter your name: ")
print("Hello,", user_name + "!")
print("Type of user_name:", type(user_name))
print()

# Collecting numeric input (initially as string)
user_age_str = input("Please enter your age: ")
print("You entered:", user_age_str)
print("Type of user_age_str:", type(user_age_str))
print()

# Note: input() always returns a string
favorite_number_str = input("Enter your favorite number: ")
print("Your favorite number is:", favorite_number_str)
print("Type:", type(favorite_number_str))
print()

print("Notice: All input() results are strings!")
