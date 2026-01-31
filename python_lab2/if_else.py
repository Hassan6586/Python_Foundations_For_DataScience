# If-else statement example
score = int(input("Enter your test score (0-100): "))

if score >= 60:
    print("Congratulations! You passed the test.")
    print(f"Your score: {score}")
else:
    print("Sorry, you did not pass the test.")
    print(f"Your score: {score}")
    print("Better luck next time!")

print("End of grade report.")
