# Interactive Calculator with Type Conversion

print("=== Simple Calculator ===")
print()

# Get user input and convert to numbers
print("Let's perform some basic calculations!")
num1_str = input("Enter the first number: ")
num2_str = input("Enter the second number: ")

# Convert strings to floats for calculation
num1 = float(num1_str)
num2 = float(num2_str)

print()
print("Input Analysis:")
print("First input:", num1_str, "| Type:", type(num1_str))
print("After conversion:", num1, "| Type:", type(num1))
print("Second input:", num2_str, "| Type:", type(num2_str))
print("After conversion:", num2, "| Type:", type(num2))
print()

# Perform calculations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2

print("Calculation Results:")
print(f"{num1} + {num2} = {addition}")
print(f"{num1} - {num2} = {subtraction}")
print(f"{num1} * {num2} = {multiplication}")
print(f"{num1} / {num2} = {division}")
print()

# Convert results back to different types
print("Type Conversion of Results:")
print("Addition as integer:", int(addition))
print("Addition as string:", str(addition))
