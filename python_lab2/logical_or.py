# Using logical OR operator
day = input("What day is it? ").lower()

if day == "saturday" or day == "sunday":
    print("It's the weekend! Time to relax.")
    print("No school today!")
else:
    print("It's a weekday. Time for school or work.")
    
# Another example with numbers
number = int(input("Enter a number: "))

if number < 0 or number > 100:
    print("Number is outside the range 0-100")
else:
    print("Number is within the acceptable range")
