# Advanced Temperature Categorization Program
print("=== Advanced Temperature Categorizer ===")
print()

# Get inputs
temperature = float(input("Enter temperature in Fahrenheit: "))
humidity = float(input("Enter humidity percentage (0-100): "))
is_sunny = input("Is it sunny? (yes/no): ").lower()

print("\n--- Analysis ---")

# Main temperature categorization with nested conditions
if temperature >= 80:
    print(f"{temperature}°F is HOT")
    
    # Nested conditions for hot weather
    if humidity > 70:
        print("High humidity makes it feel even hotter!")
        comfort_level = "Very Uncomfortable"
    elif humidity > 50:
        print("Moderate humidity - quite warm")
        comfort_level = "Uncomfortable"
    else:
        print("Low humidity - dry heat")
        comfort_level = "Tolerable"
        
    # Additional nested condition
    if is_sunny == "yes" and temperature > 90:
        print("WARNING: Extremely hot and sunny - stay hydrated!")
        
elif temperature <= 50:
    print(f"{temperature}°F is COLD")
    
    # Nested conditions for cold weather
    if temperature <= 32:
        print("Below freezing! Ice may form.")
        if humidity > 80:
            print("High humidity - feels very cold and damp")
            comfort_level = "Very Cold"
        else:
            print("Dry cold weather")
            comfort_level = "Cold"
    else:
        print("Chilly but above freezing")
        comfort_level = "Cool"
        
    # Wind consideration
    if is_sunny == "no":
        print("Cloudy and cold - dress warmly!")
        
else:
    print(f"{temperature}°F is MILD")
    
    # Nested conditions for mild weather
    if temperature >= 70 and humidity < 60 and is_sunny == "yes":
        print("Perfect weather conditions!")
        comfort_level = "Perfect"
    elif humidity > 80:
        print("A bit humid but comfortable temperature")
        comfort_level = "Slightly Humid"
    else:
        print("Pleasant temperature")
        comfort_level = "Comfortable"

# Final recommendations using logical operators
print(f"\nComfort Level: {comfort_level}")
print("\n--- Recommendations ---")

if temperature > 85 and humidity > 70:
    print("• Stay indoors with air conditioning")
    print("• Drink plenty of water")
elif temperature < 40 or (temperature < 50 and is_sunny == "no"):
    print("• Wear warm clothing")
    print("• Consider staying inside")
elif temperature >= 60 and temperature <= 75 and humidity < 70:
    print("• Great weather for outdoor activities!")
    print("• Perfect for a walk or picnic")
else:
    print("• Dress appropriately for the weather")
    print("• Check conditions before going out")

print("\nThank you for using the Temperature Categorizer!")
