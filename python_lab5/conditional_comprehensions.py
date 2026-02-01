#!/usr/bin/env python3
"""
Conditional Logic in Comprehensions Laboratory
This script demonstrates various conditional logic patterns in list and dictionary comprehensions
"""

def filtering_comprehensions():
    """Demonstrate filtering using conditional logic"""
    
    print("=== Filtering with Conditional Logic ===\n")
    
    # Sample data
    students_data = [
        {'name': 'Alice', 'age': 20, 'grade': 85, 'major': 'Computer Science'},
        {'name': 'Bob', 'age': 22, 'grade': 92, 'major': 'Mathematics'},
        {'name': 'Charlie', 'age': 19, 'grade': 78, 'major': 'Physics'},
        {'name': 'Diana', 'age': 21, 'grade': 96, 'major': 'Computer Science'},
        {'name': 'Eve', 'age': 20, 'grade': 88, 'major': 'Chemistry'},
        {'name': 'Frank', 'age': 23, 'grade': 74, 'major': 'Mathematics'}
    ]
    
    # Example 1: Simple filtering
    print("1. Students with grade >= 85:")
    high_achievers = [student['name'] for student in students_data if student['grade'] >= 85]
    for name in high_achievers:
        print(f"   {name}")
    print()
    
    # Example 2: Multiple conditions with AND
    print("2. Computer Science students with grade >= 85:")
    cs_high_achievers = [
        student['name'] for student in students_data 
        if student['major'] == 'Computer Science' and student['grade'] >= 85
    ]
    for name in cs_high_achievers:
        print(f"   {name}")
    print()
    
    # Example 3: Multiple conditions with OR
    print("3. Students who are either very young (< 20) or high achievers (>= 90):")
    special_students = [
        f"{student['name']} (Age: {student['age']}, Grade: {student['grade']})"
        for student in students_data 
        if student['age'] < 20 or student['grade'] >= 90
    ]
    for student in special_students:
        print(f"   {student}")
    print()
    
    # Example 4: Complex filtering with string operations
    print("4. Students whose names start with vowels and have grades > 80:")
    vowel_students = [
        student for student in students_data 
        if student['name'][0].lower() in 'aeiou' and student['grade'] > 80
    ]
    for student in vowel_students:
        print(f"   {student['name']}: {student['grade']}")
    print()
    
    return high_achievers, cs_high_achievers, special_students

def conditional_expressions():
    """Demonstrate conditional expressions in comprehensions"""
    
    print("=== Conditional Expressions (if-else) ===\n")
    
    # Sample data
    temperatures = [32, 68, 85, 100, 212, 0, -10, 45, 75, 90]
    
    # Example 1: Simple conditional expression
    print("1. Temperature descriptions:")
    temp_descriptions = [
        f"{temp}°F - {'Hot' if temp > 80 else 'Cool'}" 
        for temp in temperatures
    ]
    for desc in temp_descriptions:
        print(f"   {desc}")
    print()
    
    # Example 2: Multiple conditional expressions (nested)
    print("2. Detailed temperature categories:")
    detailed_temps = [
        f"{temp}°F - {'Freezing' if temp <= 32 else 'Cold' if temp < 50 else 'Warm' if temp < 80 else 'Hot'}"
        for temp in temperatures
    ]
    for desc in detailed_temps:
        print(f"   {desc}")
    print()
    
    # Example 3: Conditional expressions with calculations
    print("3. Celsius conversions (only for temps above freezing):")
    celsius_temps = [
        f"{temp}°F = {(temp-32)*5/9:.1f}°C" if temp > 32 else f"{temp}°F (Below freezing)"
        for temp in temperatures
    ]
    for temp in celsius_temps:
        print(f"   {temp}")
    print()
    
    # Example 4: Dictionary comprehension with conditional expressions
    print("4. Temperature status dictionary:")
    temp_status = {
        temp: 'Safe' if 32 < temp < 100 else 'Extreme'
        for temp in temperatures
    }
    for temp, status in temp_status.items():
        print(f"   {temp}°F: {status}")
    print()
    
    return temp_descriptions, detailed_temps, temp_status

def advanced_conditional_patterns():
    """Demonstrate advanced conditional patterns"""
    
    print("=== Advanced Conditional Patterns ===\n")
    
    # Sample data: Product inventory
    inventory = [
        {'name': 'Laptop', 'price': 999.99, 'stock': 5, 'category': 'Electronics'},
        {'name': 'Book', 'price': 15.99, 'stock': 50, 'category': 'Education'},
        {'name': 'Headphones', 'price': 199.99, 'stock': 0, 'category': 'Electronics'},
        {'name': 'Desk Chair', 'price': 299.99, 'stock': 8, 'category': 'Furniture'},
        {'name': 'Notebook', 'price': 5.99, 'stock': 100, 'category': 'Education'},
        {'name': 'Monitor', 'price': 399.99, 'stock': 3, 'category': 'Electronics'}
    ]
    
    # Example 1: Complex filtering with multiple conditions
    print("1. Available Electronics under $500:")
    available_electronics = [
        f"{item['name']} - ${item['price']} (Stock: {item['stock']})"
        for item in inventory
        if item['category'] == 'Electronics' and item['stock'] > 0 and item['price'] < 500
    ]
    for item in available_electronics:
        print(f"   {item}")
    print()
    
    # Example 2: Nested comprehensions with conditions
    print("2. Category-wise available items:")
    categories = list(set(item['category'] for item in inventory))
    
    category_items = {
        category: [
            f"{item['name']} (${item['price']})"
            for item in inventory
            if item['category'] == category and item['stock'] > 0
        ]
        for category in categories
    }
    
    for category, items in category_items.items():
        print(f"   {category}:")
        for item in items:
            print(f"     - {item}")
    print()
    
    return available_electronics, category_items

def interactive_conditional_comprehension():
    """Interactive function to practice conditional comprehensions"""
    
    print("=== Interactive Conditional Comprehension Practice ===")
    
    # Sample data for practice
    sample_numbers = list(range(1, 101))
    
    print("Available operations:")
    print("1. Filter even numbers")
    print("2. Filter numbers divisible by a specific value")
    print("3. Transform numbers with conditions")
    print("4. Create custom filter")
    
    try:
        choice = input("Choose an operation (1-4): ").strip()
        
        if choice == '1':
            result = [num for num in sample_numbers if num % 2 == 0]
            print(f"Even numbers (1-100): {result[:10]}... (showing first 10)")
            print(f"Total count: {len(result)}")
            
        elif choice == '2':
            divisor = int(input("Enter divisor: "))
            result = [num for num in sample_numbers if num % divisor == 0]
            print(f"Numbers divisible by {divisor}: {result}")
            print(f"Total count: {len(result)}")
            
        elif choice == '3':
            result = [
                f"{num} is {'even' if num % 2 == 0 else 'odd'}" 
                for num in sample_numbers[:20]  # First 20 for readability
            ]
            print("Number classifications (first 20):")
            for item in result:
                print(f"   {item}")
                
        elif choice == '4':
            min_val = int(input("Enter minimum value: "))
            max_val = int(input("Enter maximum value: "))
            condition = input("Enter condition (even/odd/all): ").lower()
            
            if condition == 'even':
                result = [num for num in sample_numbers if min_val <= num <= max_val and num % 2 == 0]
            elif condition == 'odd':
                result = [num for num in sample_numbers if min_val <= num <= max_val and num % 2 != 0]
            else:
                result = [num for num in sample_numbers if min_val <= num <= max_val]
            
            print(f"Numbers between {min_val} and {max_val} ({condition}): {result}")
            print(f"Total count: {len(result)}")
            
        else:
            print("Invalid choice. Please select 1-4.")
            
    except ValueError:
        print("Error: Please enter valid integers.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Run all demonstrations
    filtering_comprehensions()
    conditional_expressions()
    advanced_conditional_patterns()
    
    # Run interactive practice
    interactive_conditional_comprehension()
    
    print("\n=== Lab Task 3 Completed Successfully ===")
