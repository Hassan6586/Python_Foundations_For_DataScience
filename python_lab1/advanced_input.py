# Advanced Input Handling

print("=== Advanced Input Handling ===")
print()

# Collecting and displaying multiple inputs
print("Student Registration System")
print("-" * 30)

student_name = input("Student Name: ")
student_id = input("Student ID: ")
email = input("Email Address: ")

print()
print("Registration Summary:")
print("Name:", student_name)
print("ID:", student_id)
print("Email:", email)
print()

# Demonstrating input with prompts
course_selection = input("Select your course (CS/IT/ENG): ")
semester = input("Enter semester (Fall/Spring/Summer): ")

print()
print("Course Information:")
print("Selected Course:", course_selection)
print("Semester:", semester)
print()

# Boolean-like input
is_full_time = input("Are you a full-time student? (yes/no): ")
print("Full-time status:", is_full_time)
print("Type:", type(is_full_time))
