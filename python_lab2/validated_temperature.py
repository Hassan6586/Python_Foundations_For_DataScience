# Temperature Categorizer with Input Validation
print("=== Temperature Categorizer with Validation ===")

def get_valid_temperature():
    while True:
        try:
            temp = float(input("Enter temperature in Fahrenheit (-100 to 150): "))
            if temp < -100 or temp > 150:
                print("Please enter a realistic temperature between -100°F and 150°F")
                continue
            return temp
        except ValueError:
            print("Please enter a valid number for temperature")

def get_valid_humidity():
    while True:
        try:
            humidity = float(input("Enter humidity percentage (0-100): "))
            if humidity < 0 or humidity > 100:
                print("Humidity must be between 0 and 100 percent")
                continue
            return humidity
        except ValueError:
            print("Please enter a valid number for humidity")

def get_yes_no_input(prompt):
    while True:
        response = input(prompt).lower().strip()
        if response in ['yes', 'y', 'no', 'n']:
            return response in ['yes', 'y']
        print("Please enter 'yes' or 'no'")

# Get validated inputs
temperature = get_valid_temperature()
humidity = get_valid_humidity()
is_sunny = get_yes_no_input("Is it sunny? (yes/no): ")

# Process the data (same logic as before)
print(f"\n--- Analysis for {temperature}°F ---")

if temperature >= 80:
    category = "HOT"
    if humidity > 70 and temperature > 90:
        advice = "Dangerous heat index - avoid outdoor activities"
    elif humidity > 50:
        advice = "Stay cool and hydrated"
    else:
        advice = "Hot but manageable"
elif temperature <= 50:
    category = "COLD"
    if temperature <= 32 and humidity > 80:
        advice = "Freezing and damp - dress very warmly"
    elif temperature <= 32:
        advice = "Below freezing - watch for ice"
    else:
        advice = "Cold weather - wear layers"
else:
    category = "MILD"
    if 65 <= temperature <= 75 and humidity < 60 and is_sunny:
        advice = "Perfect weather - enjoy outdoor activities!"
    else:
        advice = "Pleasant temperature"

print(f"Category: {category}")
print(f"Advice: {advice}")

# Complex condition example
if (temperature > 90 and humidity > 80) or (temperature < 20):
    print("⚠️  WEATHER ALERT: Extreme conditions detected!")
elif temperature >= 65 and temperature <= 75 and not (humidity > 70):
    print("✅ Ideal weather conditions!")

print("\nProgram completed successfully!")
