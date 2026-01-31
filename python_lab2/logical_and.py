# Using logical AND operator
username = input("Enter username: ")
password = input("Enter password: ")
age = int(input("Enter your age: "))

# Check multiple conditions
if username == "student" and password == "python123" and age >= 13:
    print("Access granted!")
    print("Welcome to the Python learning platform.")
else:
    print("Access denied!")
    if username != "student":
        print("- Invalid username")
    if password != "python123":
        print("- Invalid password")
    if age < 13:
        print("- You must be at least 13 years old")
