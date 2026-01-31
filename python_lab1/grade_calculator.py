# Student Grade Calculator - Practical Application

print("=== Student Grade Calculator ===")
print()

# Collect student information
student_name = input("Enter student name: ")
student_id = input("Enter student ID: ")
course_name = input("Enter course name: ")

print()
print("Enter your scores for different assessments:")

# Collect scores as strings and convert to floats
quiz1_str = input("Quiz 1 score (out of 100): ")
quiz2_str = input("Quiz 2 score (out of 100): ")
midterm_str = input("Midterm score (out of 100): ")
final_str = input("Final exam score (out of 100): ")
project_str = input("Project score (out of 100): ")

# Convert all inputs to float
quiz1 = float(quiz1_str)
quiz2 = float(quiz2_str)
midterm = float(midterm_str)
final = float(final_str)
project = float(project_str)

print()
print("=== Grade Calculation ===")
print()

# Display input verification
print("Input Verification:")
print(f"Quiz 1: {quiz1} | Type: {type(quiz1)}")
print(f"Quiz 2: {quiz2} | Type: {type(quiz2)}")
print(f"Midterm: {midterm} | Type: {type(midterm)}")
print(f"Final: {final} | Type: {type(final)}")
print(f"Project: {project} | Type: {type(project)}")
print()

# Calculate weighted average
# Weights: Quizzes 20%, Midterm 25%, Final 35%, Project 20%
quiz_average = (quiz1 + quiz2) / 2
weighted_score = (quiz_average * 0.20) + (midterm * 0.25) + (final * 0.35) + (project * 0.20)

# Determine letter grade
if weighted_score >= 90:
    letter_grade = "A"
elif weighted_score >= 80:
    letter_grade = "B"
elif weighted_score >= 70:
    letter_grade = "C"
elif weighted_score >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

# Determine pass/fail status
is_passing = weighted_score >= 60

print("=== Final Grade Report ===")
print(f"Student: {student_name}")
print(f"ID: {student_id}")
print(f"Course: {course_name}")
print()
print("Score Breakdown:")
print(f"Quiz Average: {quiz_average:.2f}")
print(f"Midterm: {midterm}")
print(f"Final: {final}")
print(f"Project: {project}")
print()
print(f"Weighted Final Score: {weighted_score:.2f}")
print(f"Letter Grade: {letter_grade}")
print(f"Passing Status: {is_passing}")
print(f"Status Type: {type(is_passing)}")

# Type conversion examples in context
print()
print("=== Type Conversion Examples ===")
print(f"Final score as integer: {int(weighted_score)}")
print(f"Final score as string: '{str(weighted_score)}'")
print(f"Passing status as integer: {int(is_passing)}")
print(f"Passing status as string: '{str(is_passing)}'")
