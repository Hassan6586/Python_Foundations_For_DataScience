# Using logical NOT operator
is_raining = input("Is it raining? (yes/no): ").lower()

if not is_raining == "yes":
    print("Great! You can go outside without an umbrella.")
    print("Perfect weather for outdoor activities!")
else:
    print("Better take an umbrella!")
    print("Maybe it's a good day to stay inside and code.")

# Another way to write the same logic
if is_raining != "yes":
    print("(This is another way to check the same condition)")
