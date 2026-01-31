# Debug Practice - Fix the errors in this code
temperature = input("Enter temperature: ")  # Error 1: Should convert to float
humidity = float(input("Enter humidity: "))

if temperature > 80  # Error 2: Missing colon
print("It's hot!")   # Error 3: Wrong indentation

if humidity > 70 and temperature > 85:
    print("Very uncomfortable weather")
elif humidity < 30 or temperature < 40
    print("Dry or cold conditions")  # Error 4: Missing colon above

# Error 5: Logic error - this will never execute
if temperature > 100:
    print("Extremely hot")
elif temperature > 90:
    print("Very hot")
elif temperature > 100:  # This condition will never be reached
    print("This will never print")

print("Program finished")
