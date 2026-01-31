# Temperature Categorization Program
print("=== Temperature Categorizer ===")
print("This program will categorize temperature as hot, cold, or mild.")
print()

# Get temperature input
temperature = float(input("Enter temperature in Fahrenheit: "))

# Basic categorization
if temperature >= 80:
    category = "hot"
    print(f"{temperature}°F is considered HOT")
elif temperature <= 50:
    category = "cold"
    print(f"{temperature}°F is considered COLD")
else:
    category = "mild"
    print(f"{temperature}°F is considered MILD")

print(f"Temperature category: {category.upper()}")
