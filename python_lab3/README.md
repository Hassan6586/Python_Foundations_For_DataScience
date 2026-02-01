# Lab 3: Looping Through Data

## Overview
This lab focuses on mastering loop structures in Python, including for loops, while loops, and loop control statements (break and continue). You'll build practical applications like sum calculators, countdown timers, and data validation systems.

## Learning Objectives
- Understand the fundamental concepts of loops in programming
- Implement for loops to iterate through data collections
- Create while loops for conditional repetition
- Use break and continue statements to control loop execution
- Sum numbers in a list using iterative techniques
- Build a functional countdown timer application
- Apply loop control statements effectively in real-world scenarios

## Lab Files

### Task 1: For Loops
- **sum_numbers.py** - Sum calculator with three parts:
  - Basic for loop demonstration
  - Sum calculation with step-by-step output
  - Interactive sum calculator with user input

### Task 2: While Loops
- **countdown_timer.py** - Countdown timer with two versions:
  - Basic while loop countdown
  - Enhanced timer with minutes:seconds format
- **simple_countdown.py** - Simplified countdown for beginners

### Task 3: Loop Control
- **loop_control.py** - Break and continue examples:
  - Search with break statement
  - Filter with continue statement
  - Data validation system combining both
- **nested_loops.py** - Multiplication table generator with nested loop control

### Testing
- **test_all_loops.py** - Comprehensive automated tests for all loop types

## How to Run

Navigate to the python_lab3 directory and run any script:

```bash
cd python_lab3

# Task 1: For loops
python3 sum_numbers.py
# Enter numbers when prompted, type 'done' to finish

# Task 2: While loops
python3 countdown_timer.py
# Enter countdown duration (e.g., 10)

python3 simple_countdown.py
# Enter countdown duration (e.g., 5)

# Task 3: Loop control
python3 loop_control.py
# Follow prompts to test break/continue

python3 nested_loops.py
# View multiplication tables with loop control

# Run all tests
python3 test_all_loops.py
```

## Key Concepts

### For Loop
```python
# Iterate through a list
for item in list:
    # process item
```

### While Loop
```python
# Loop while condition is true
while condition:
    # execute code
    # update condition
```

### Break Statement
```python
# Exit loop immediately
for item in items:
    if condition:
        break  # stops loop
```

### Continue Statement
```python
# Skip to next iteration
for item in items:
    if condition:
        continue  # skips rest of current iteration
```

## Testing Examples

### Sum Calculator
```
Input: 10, 20, 30, done
Output: Sum = 60, Average = 20.00
```

### Countdown Timer
```
Input: 10
Output: Counts down from 10 to 1, then "Time's up!"
```

### Data Validator
```
Valid range: 1-100
Commands: 'quit' to exit, 'skip' to skip
Test with: 50, 150 (out of range), skip, 75, quit
```

### Multiplication Tables
```
Generates tables 1-5
Skips multiplying by 7
Stops if result > 30
Asks to continue between tables
```

## Common Loop Patterns

### Sum Pattern
```python
total = 0
for number in numbers:
    total += number
```

### Search Pattern
```python
for item in items:
    if item == target:
        print("Found!")
        break
```

### Filter Pattern
```python
for item in items:
    if not meets_criteria(item):
        continue
    process(item)
```

### Countdown Pattern
```python
count = start
while count > 0:
    print(count)
    count -= 1
```

## Common Errors to Avoid

### 1. Infinite Loops
```python
# Wrong - infinite loop
count = 5
while count > 0:
    print(count)
    # Missing: count -= 1

# Correct
count = 5
while count > 0:
    print(count)
    count -= 1
```

### 2. Index Errors
```python
# Risky
numbers = [1, 2, 3]
for i in range(10):  # Error if accessing numbers[i]
    print(numbers[i])

# Safe
for number in numbers:
    print(number)
```

### 3. Break/Continue Outside Loop
```python
# Wrong - SyntaxError
if condition:
    break

# Correct
for item in items:
    if condition:
        break
```

## Prerequisites
- Basic understanding of Python syntax
- Knowledge of variables and data types
- Familiarity with lists and basic data structures
- Understanding of conditional statements (if/else)

## Next Steps
After mastering loops, you're ready to:
- Work with nested data structures
- Create more complex algorithms
- Build data processing pipelines
- Develop automation scripts
- Learn about functions and modules

## Troubleshooting

### Issue: Program won't stop
**Cause:** Infinite loop
**Solution:** Ensure loop condition eventually becomes false

### Issue: KeyboardInterrupt error
**Cause:** User pressed Ctrl+C
**Solution:** This is normal - use to stop infinite loops

### Issue: List index out of range
**Cause:** Accessing index that doesn't exist
**Solution:** Use `for item in list:` instead of indexing

## Author
Lab created for Python programming course

## License
Educational use only
