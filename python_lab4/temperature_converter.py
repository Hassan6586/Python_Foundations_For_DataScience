# Temperature Converter - Basic Functions

# Part 1: Basic function demonstration
def greet_user():
    """This function greets the user"""
    print("Welcome to the Temperature Converter Lab!")
    print("Let's learn about functions together!")
    print()

# Call the function
greet_user()

# Part 2: Celsius to Fahrenheit conversion
def celsius_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit
    Formula: F = (C × 9/5) + 32
    """
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Test the function
print("=== Celsius to Fahrenheit ===")
temp_celsius = 25
temp_fahrenheit = celsius_to_fahrenheit(temp_celsius)
print(f"{temp_celsius}°C is equal to {temp_fahrenheit}°F")
print()

# Part 3: Fahrenheit to Celsius conversion
def fahrenheit_to_celsius(fahrenheit):
    """
    Convert temperature from Fahrenheit to Celsius
    Formula: C = (F - 32) × 5/9
    """
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Test the function
print("=== Fahrenheit to Celsius ===")
temp_fahrenheit = 77
temp_celsius = fahrenheit_to_celsius(temp_fahrenheit)
print(f"{temp_fahrenheit}°F is equal to {temp_celsius:.2f}°C")
print()

# Part 4: Safe conversion with validation
def safe_celsius_to_fahrenheit(celsius):
    """
    Safely convert Celsius to Fahrenheit with validation
    """
    try:
        # Check if input is a number
        celsius = float(celsius)
        
        # Check for absolute zero limit
        if celsius < -273.15:
            return None, "Error: Temperature below absolute zero (-273.15°C)"
        
        fahrenheit = (celsius * 9/5) + 32
        return fahrenheit, "Success"
    
    except ValueError:
        return None, "Error: Please enter a valid number"

# Test the improved function
print("=== Safe Conversion with Validation ===")
test_values = [25, "abc", -300, 0]

for value in test_values:
    result, message = safe_celsius_to_fahrenheit(value)
    if result is not None:
        print(f"{value}°C = {result}°F")
    else:
        print(f"Input: {value} - {message}")
