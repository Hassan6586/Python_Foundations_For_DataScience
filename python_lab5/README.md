# Lab 5: List and Dictionary Comprehensions

## Overview
This lab focuses on mastering Python comprehensions for efficient data manipulation and transformation. You'll learn to write concise, Pythonic code using list and dictionary comprehensions.

## Learning Objectives
- Understand list comprehension syntax and structure
- Create dictionary comprehensions from multiple data sources
- Apply conditional logic within comprehensions
- Filter and transform data efficiently
- Compare comprehensions with traditional loops

## Lab Files

### Task 1: List Comprehensions
- **even_extractor.py** - Extract even numbers using various comprehension techniques
  - Basic list comprehensions
  - Comprehensions with transformations
  - Multiple conditions
  - String formatting
  - Interactive even number finder

### Task 2: Dictionary Comprehensions
- **dict_comprehension.py** - Build dictionaries from lists
  - Basic dictionary creation
  - Conditional dictionary creation
  - Advanced nested dictionaries
  - Interactive dictionary builder

### Task 3: Conditional Logic
- **conditional_comprehensions.py** - Advanced filtering and expressions
  - Filter with conditional logic
  - Conditional expressions (if-else)
  - Complex filtering patterns
  - Interactive practice tool

## How to Run

Navigate to the python_lab5 directory and run any script:

```bash
cd python_lab5

# Task 1: Even number extraction
python3 even_extractor.py
# Input: 1 2 3 4 5 6 7 8 9 10

# Task 2: Dictionary comprehensions
python3 dict_comprehension.py
# Input keys: name, age, city
# Input values: John, 25, Boston

# Task 3: Conditional comprehensions
python3 conditional_comprehensions.py
# Choose operation and follow prompts
```

## Key Concepts

### List Comprehension Syntax
```python
# Basic: [expression for item in iterable]
squares = [x**2 for x in range(10)]

# With condition: [expression for item in iterable if condition]
evens = [x for x in range(10) if x % 2 == 0]

# With if-else: [expression1 if condition else expression2 for item in iterable]
labels = ['even' if x % 2 == 0 else 'odd' for x in range(10)]
```

### Dictionary Comprehension Syntax
```python
# Basic: {key: value for item in iterable}
squares_dict = {x: x**2 for x in range(5)}

# From two lists: {k: v for k, v in zip(keys, values)}
name_age = {name: age for name, age in zip(names, ages)}

# With condition: {k: v for item in iterable if condition}
filtered = {k: v for k, v in dict.items() if v > 10}
```

## Testing Examples

### Even Number Extraction
```
Input: 1 2 3 4 5 6 7 8 9 10
Output: Even numbers: [2, 4, 6, 8, 10]
        Count: 5
        Percentage: 50.0%
```

### Dictionary Creation
```
Input keys: product, price, stock
Input values: Laptop, 999.99, 5
Output: {'product': 'Laptop', 'price': 999.99, 'stock': 5}
```

### Conditional Filtering
```
Operation: Filter even numbers
Output: [2, 4, 6, 8, 10, ...] (first 10 shown)
        Total count: 50
```

## Comprehension vs Loop Comparison

### Traditional Loop
```python
result = []
for num in numbers:
    if num % 2 == 0:
        result.append(num)
```

### List Comprehension
```python
result = [num for num in numbers if num % 2 == 0]
```

**Benefits:**
- More concise and readable
- Slightly faster execution
- More Pythonic style
- Less error-prone

## Common Patterns

### Filtering
```python
# Get all positive numbers
positives = [x for x in numbers if x > 0]

# Get names starting with 'A'
a_names = [name for name in names if name.startswith('A')]
```

### Transformation
```python
# Convert to uppercase
upper_names = [name.upper() for name in names]

# Calculate totals
totals = [item['price'] * item['qty'] for item in items]
```

### Nested Comprehensions
```python
# Flatten 2D list
flat = [num for row in matrix for num in row]

# Create multiplication table
table = [[i*j for j in range(1, 11)] for i in range(1, 11)]
```

## Prerequisites
- Basic Python syntax and data types
- Understanding of lists and dictionaries
- Familiarity with for loops
- Knowledge of conditional statements

## Next Steps
After mastering comprehensions, you're ready to:
- Work with file operations
- Process CSV and JSON data
- Build data analysis tools
- Create more complex data structures

## Performance Notes
- Comprehensions are generally faster than equivalent loops
- For very large datasets, consider generators
- Readability should not be sacrificed for brevity

## Author
Lab created for Python programming course

## License
Educational use only
