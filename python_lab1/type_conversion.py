# Type Conversion Demonstration

print("=== Type Conversion Examples ===")
print()

# String to Integer conversion
age_str = "25"
age_int = int(age_str)
print("Original string:", age_str, "| Type:", type(age_str))
print("Converted to int:", age_int, "| Type:", type(age_int))
print()

# String to Float conversion
price_str = "19.99"
price_float = float(price_str)
print("Original string:", price_str, "| Type:", type(price_str))
print("Converted to float:", price_float, "| Type:", type(price_float))
print()

# Integer to String conversion
score = 95
score_str = str(score)
print("Original integer:", score, "| Type:", type(score))
print("Converted to string:", score_str, "| Type:", type(score_str))
print()

# Float to Integer conversion (truncates decimal)
gpa = 3.87
gpa_int = int(gpa)
print("Original float:", gpa, "| Type:", type(gpa))
print("Converted to int:", gpa_int, "| Type:", type(gpa_int))
print("Note: Decimal part is truncated, not rounded!")
print()

# Boolean conversions
print("Boolean Conversion Examples:")
print("int(True):", int(True))
print("int(False):", int(False))
print("bool(1):", bool(1))
print("bool(0):", bool(0))
print("bool('Hello'):", bool("Hello"))
print("bool(''):", bool(""))
