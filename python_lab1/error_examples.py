# Common Type Conversion Errors and Solutions

print("=== Error Handling Examples ===")
print()

# Example 1: Safe integer conversion
print("Example 1: Safe Integer Conversion")
user_input = input("Enter a number: ")

try:
    number = int(user_input)
    print(f"Successfully converted '{user_input}' to integer: {number}")
    print(f"Type: {type(number)}")
except ValueError:
    print(f"Error: '{user_input}' cannot be converted to an integer")
    print("Please enter a valid whole number")

print()

# Example 2: Safe float conversion
print("Example 2: Safe Float Conversion")
user_input2 = input("Enter a decimal number: ")

try:
    decimal_number = float(user_input2)
    print(f"Successfully converted '{user_input2}' to float: {decimal_number}")
    print(f"Type: {type(decimal_number)}")
except ValueError:
    print(f"Error: '{user_input2}' cannot be converted to a float")
    print("Please enter a valid number")

print()

# Example 3: Boolean conversion behavior
print("Example 3: Boolean Conversion Behavior")
test_values = ["", "0", "False", "True", "hello", "123"]

for value in test_values:
    bool_result = bool(value)
    print(f"bool('{value}') = {bool_result}")

print()
print("Note: Only empty strings and '0' are considered False in string context")
