# Basic Operations with Different Data Types

print("=== Arithmetic Operations ===")
print()

# Integer operations
a = 10
b = 3
print("Integer Operations:")
print(f"a = {a}, b = {b}")
print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")
print(f"Floor Division: {a} // {b} = {a // b}")
print(f"Modulus: {a} % {b} = {a % b}")
print(f"Exponentiation: {a} ** {b} = {a ** b}")
print()

# Float operations
x = 15.5
y = 2.5
print("Float Operations:")
print(f"x = {x}, y = {y}")
print(f"Addition: {x} + {y} = {x + y}")
print(f"Subtraction: {x} - {y} = {x - y}")
print(f"Multiplication: {x} * {y} = {x * y}")
print(f"Division: {x} / {y} = {x / y}")
print()

# Mixed operations (int and float)
print("Mixed Operations (int and float):")
result1 = a + x  # int + float
result2 = b * y  # int * float
print(f"int + float: {a} + {x} = {result1} | Type: {type(result1)}")
print(f"int * float: {b} * {y} = {result2} | Type: {type(result2)}")
print()

# String operations
first_name = "John"
last_name = "Doe"
print("String Operations:")
print(f"Concatenation: '{first_name}' + ' ' + '{last_name}' = '{first_name + ' ' + last_name}'")
print(f"Repetition: '{first_name}' * 3 = '{first_name * 3}'")
print(f"Length: len('{first_name}') = {len(first_name)}")
