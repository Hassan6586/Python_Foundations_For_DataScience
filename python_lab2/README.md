# Lab 2: Control Flow in Python

## Overview
This lab focuses on mastering conditional statements, logical operators, and control flow structures in Python. You'll build a comprehensive temperature categorization system that demonstrates real-world decision-making logic.

## Learning Objectives
- Understand and implement conditional statements (if, elif, else)
- Use comparison operators to evaluate conditions
- Apply logical operators (and, or, not) to combine multiple conditions
- Create nested if statements for complex decision-making
- Write a temperature categorization program using control flow structures
- Debug and troubleshoot common control flow errors

## Lab Files

### Task 1: Basic Conditional Statements
- **simple_if.py** - Introduction to if statements
- **if_else.py** - Handling true and false conditions
- **grade_system.py** - Multiple conditions with elif

### Task 2: Logical Operators
- **logical_and.py** - Using the AND operator for multiple conditions
- **logical_or.py** - Using the OR operator for alternative conditions
- **logical_not.py** - Using the NOT operator to reverse conditions

### Task 3: Temperature Categorization Program
- **temperature_categorizer.py** - Basic temperature categories
- **advanced_temperature.py** - Enhanced version with nested conditions
- **validated_temperature.py** - Complete version with input validation

### Task 4: Debugging Practice
- **debug_practice.py** - Code with intentional errors for practice
- **debug_practice_corrected.py** - Corrected version with explanations

## How to Run

Navigate to the python_lab2 directory and run any script:

```bash
cd python_lab2

# Basic examples
python3 simple_if.py
python3 if_else.py
python3 grade_system.py

# Logical operators
python3 logical_and.py
python3 logical_or.py
python3 logical_not.py

# Temperature programs
python3 temperature_categorizer.py
python3 advanced_temperature.py
python3 validated_temperature.py

# Debug practice
python3 debug_practice.py  # This has errors!
python3 debug_practice_corrected.py  # Fixed version
```

## Key Concepts

### Conditional Statements
```python
if condition:
    # code block
elif another_condition:
    # code block
else:
    # code block
```

### Logical Operators
- **and** - All conditions must be true
- **or** - At least one condition must be true
- **not** - Reverses the condition

### Nested Conditions
```python
if outer_condition:
    if inner_condition:
        # nested code
    else:
        # nested code
```

## Testing Examples

### Grade System
Test with scores: 95, 85, 75, 65, 55

### Logical AND
Test combinations:
- Correct: username="student", password="python123", age=16
- Wrong username: username="admin", password="python123", age=16

### Temperature Categorizer
Test scenarios:
- Hot and humid: temp=95, humidity=80, sunny=yes
- Cold and dry: temp=25, humidity=30, sunny=no
- Perfect weather: temp=72, humidity=45, sunny=yes

## Common Errors to Avoid

1. **IndentationError** - Inconsistent spacing
2. **Using = instead of ==** - Assignment vs comparison
3. **Missing colons** - After if/elif/else statements
4. **Unreachable conditions** - Order matters in elif chains

## Prerequisites
- Basic understanding of Python syntax and variables
- Knowledge of data types (strings, integers, floats)
- Familiarity with input() and print() functions
- Completed Lab 1 or equivalent Python fundamentals

## Next Steps
With these control flow skills, you're ready to:
- Work with loops (for and while)
- Create functions
- Build more complex decision-making systems
- Develop real-world applications

## Author
Lab created for Python programming course

## License
Educational use only
