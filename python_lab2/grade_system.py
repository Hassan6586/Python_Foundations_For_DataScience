# Multiple conditions with elif
score = int(input("Enter your test score (0-100): "))

if score >= 90:
    grade = "A"
    message = "Excellent work!"
elif score >= 80:
    grade = "B"
    message = "Good job!"
elif score >= 70:
    grade = "C"
    message = "Satisfactory performance."
elif score >= 60:
    grade = "D"
    message = "You passed, but consider studying more."
else:
    grade = "F"
    message = "You need to retake the test."

print(f"Score: {score}")
print(f"Grade: {grade}")
print(f"Comment: {message}")
