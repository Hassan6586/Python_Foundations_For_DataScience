# Lab 4: Functions and Reusability

## Overview
This lab focuses on creating reusable functions in Python, specifically for temperature conversion. You'll learn to write functions that return single and multiple values, use functions in loops, and apply best practices for code organization.

## Learning Objectives
- Understand the concept of functions and their importance
- Create custom functions for temperature conversion
- Implement functions that return multiple values
- Use functions effectively within loops
- Apply the DRY (Don't Repeat Yourself) principle
- Debug and troubleshoot function-related issues

## Lab Files

### Task 1: Basic Functions
- **temperature_converter.py** - Basic temperature conversion functions
  - Greet user function
  - Celsius to Fahrenheit
  - Fahrenheit to Celsius
  - Safe conversion with validation

### Task 2: Multiple Return Values
- **advanced_converter.py** - Functions returning multiple values
  - Multi-scale converter (C, F, K, R)
  - Universal temperature converter
  - Error handling and validation

### Task 3: Functions in Loops
- **batch_processor.py** - Batch processing with functions
  - Process lists of temperatures
  - Celsius to Fahrenheit batch conversion
  - Fahrenheit to Celsius batch conversion

- **interactive_converter.py** - Interactive menu system
  - Menu-driven interface
  - User input validation
  - Batch conversion mode

### Task 4: Best Practices
- **best_practices.py** - Advanced concepts
  - Comprehensive documentation
  - Logging functionality
  - Performance benchmarking
  - Error handling

### Practice
- **practice_exercises.py** - Practice problems
  - Temperature statistics calculator
  - Temperature range validator
  - Multi-unit converter

## How to Run

Navigate to the python_lab4 directory and run any script:

```bash
cd python_lab4

# Basic conversions
python3 temperature_converter.py

# Advanced conversions
python3 advanced_converter.py

# Batch processing
python3 batch_processor.py

# Interactive converter (menu-driven)
python3 interactive_converter.py

# Best practices examples
python3 best_practices.py

# Practice exercises
python3 practice_exercises.py
```

## Key Concepts

### Basic Function Syntax
```python
def function_name(parameters):
    """Docstring describing the function"""
    # Function body
    return result
```

### Multiple Return Values
```python
def convert_temp(celsius):
    fahrenheit = (celsius * 9/5) + 32
    kelvin = celsius + 273.15
    return fahrenheit, kelvin  # Returns tuple
```

### Function with Error Handling
```python
def safe_convert(temp):
    try:
        temp = float(temp)
        return (temp * 9/5) + 32, True
    except ValueError:
        return None, False
```

## Temperature Conversion Formulas

### Celsius ↔ Fahrenheit
- **C to F**: `F = (C × 9/5) + 32`
- **F to C**: `C = (F - 32) × 5/9`

### Celsius ↔ Kelvin
- **C to K**: `K = C + 273.15`
- **K to C**: `C = K - 273.15`

### Celsius ↔ Rankine
- **C to R**: `R = (C + 273.15) × 9/5`
- **R to C**: `C = (R × 5/9) - 273.15`

### Physical Limits
- **Absolute Zero**: -273.15°C = -459.67°F = 0K

## Testing Examples

### Basic Conversion
```
Input: 25°C
Output: 77.00°F

Input: 32°F
Output: 0.00°C
```

### Multi-Scale Conversion
```
Input: 100°C
Output:
  Fahrenheit: 212.00°F
  Kelvin: 373.15K
  Rankine: 671.67°R
```

### Batch Processing
```
Input: [0, 25, 100]°C
Output:
  0°C → 32.00°F
  25°C → 77.00°F
  100°C → 212.00°F
```

### Interactive Menu
```
1. Celsius to Fahrenheit
2. Fahrenheit to Celsius
3. Celsius to Kelvin
4. Kelvin to Celsius
5. Batch convert
6. Exit

Select option: 1
Enter temperature: 37
Result: 37°C = 98.60°F
```

## Common Errors & Solutions

### Error 1: Missing Return Statement
```python
# Wrong
def convert(c):
    f = (c * 9/5) + 32
    # Missing return!

# Correct
def convert(c):
    f = (c * 9/5) + 32
    return f
```

### Error 2: Variable Scope
```python
# Wrong
def convert(c):
    result = (c * 9/5) + 32

convert(25)
print(result)  # NameError!

# Correct
def convert(c):
    result = (c * 9/5) + 32
    return result

output = convert(25)
print(output)
```

### Error 3: Type Errors
```python
# Wrong
def convert(temp):
    return (temp * 9/5) + 32

convert("25")  # TypeError!

# Correct
def convert(temp):
    try:
        temp = float(temp)
        return (temp * 9/5) + 32
    except ValueError:
        return None
```

## Best Practices

### 1. Use Docstrings
```python
def celsius_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.
    
    Args:
        celsius (float): Temperature in Celsius
    
    Returns:
        float: Temperature in Fahrenheit
    """
    return (celsius * 9/5) + 32
```

### 2. Validate Input
```python
def safe_convert(temp):
    if temp < -273.15:
        return None, "Below absolute zero"
    return (temp * 9/5) + 32, "Success"
```

### 3. Use Meaningful Names
```python
# Good
def celsius_to_fahrenheit(celsius):
    pass

# Bad
def ctf(c):
    pass
```

### 4. Keep Functions Focused
```python
# Good - single responsibility
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

# Bad - doing too much
def convert_all_things(temp, from_unit, to_unit):
    # Too complex!
```

## Prerequisites
- Basic Python syntax and variables
- Understanding of conditional statements
- Familiarity with loops
- Knowledge of input/output operations

## Next Steps
After mastering functions, you're ready to:
- Learn about lambda functions
- Explore modules and imports
- Study object-oriented programming
- Build larger applications with multiple functions
- Create your own Python packages

## Additional Practice Ideas

1. **Distance Converter** - Create functions for km/miles/meters
2. **Weight Converter** - Create functions for kg/lbs/oz
3. **Currency Converter** - Create functions for different currencies
4. **BMI Calculator** - Create functions for health metrics
5. **Grade Calculator** - Create functions for student grades

## Author
Lab created for Python programming course

## License
Educational use only
