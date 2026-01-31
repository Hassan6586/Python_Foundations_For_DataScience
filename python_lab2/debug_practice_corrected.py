# Corrected version
temperature = float(input("Enter temperature: "))  # Fixed: Convert to float
humidity = float(input("Enter humidity: "))

if temperature > 80:  # Fixed: Added colon
    print("It's hot!")  # Fixed: Proper indentation

if humidity > 70 and temperature > 85:
    print("Very uncomfortable weather")
elif humidity < 30 or temperature < 40:  # Fixed: Added colon
    print("Dry or cold conditions")

# Fixed: Proper order of conditions
if temperature > 100:
    print("Extremely hot")
elif temperature > 90:
    print("Very hot")
# Removed unreachable condition

print("Program finished")
