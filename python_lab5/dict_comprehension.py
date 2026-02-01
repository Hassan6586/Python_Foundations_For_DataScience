#!/usr/bin/env python3
"""
Dictionary Comprehension Laboratory
This script demonstrates various dictionary comprehension techniques
"""

def basic_dictionary_creation():
    """Demonstrate basic dictionary creation from two lists"""
    
    print("=== Basic Dictionary Creation ===\n")
    
    # Example 1: Student names and grades
    students = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']
    grades = [85, 92, 78, 96, 88]
    
    # Create dictionary using comprehension
    student_grades = {student: grade for student, grade in zip(students, grades)}
    
    print("1. Student Grades Dictionary:")
    print(f"   Students: {students}")
    print(f"   Grades: {grades}")
    print(f"   Dictionary: {student_grades}")
    print(f"   Number of students: {len(student_grades)}\n")
    
    # Example 2: Product names and prices
    products = ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headphones']
    prices = [999.99, 25.50, 75.00, 299.99, 150.00]
    
    product_catalog = {product: price for product, price in zip(products, prices)}
    
    print("2. Product Catalog Dictionary:")
    for product, price in product_catalog.items():
        print(f"   {product}: ${price}")
    print()
    
    return student_grades, product_catalog

def conditional_dictionary_creation():
    """Demonstrate dictionary creation with conditions"""
    
    print("=== Conditional Dictionary Creation ===\n")
    
    # Data sets
    cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
    populations = [8419000, 3980000, 2716000, 2320000, 1680000]
    
    # Example 1: Only cities with population > 3 million
    major_cities = {city: pop for city, pop in zip(cities, populations) if pop > 3000000}
    
    print("1. Major Cities (Population > 3 million):")
    for city, pop in major_cities.items():
        print(f"   {city}: {pop:,} people")
    print()
    
    # Example 2: Dictionary with transformed values
    city_categories = {
        city: "Mega City" if pop > 5000000 else "Large City" 
        for city, pop in zip(cities, populations)
    }
    
    print("2. City Categories:")
    for city, category in city_categories.items():
        print(f"   {city}: {category}")
    print()
    
    # Example 3: Multiple conditions
    affordable_products = ['Book', 'Pen', 'Notebook', 'Calculator', 'Backpack']
    product_prices = [15.99, 2.50, 8.99, 25.00, 45.00]
    
    budget_items = {
        product: price for product, price in zip(affordable_products, product_prices) 
        if price < 20.00 and len(product) > 3
    }
    
    print("3. Budget Items (< $20 and name length > 3):")
    for item, price in budget_items.items():
        print(f"   {item}: ${price}")
    print()
    
    return major_cities, city_categories, budget_items

def advanced_dictionary_techniques():
    """Demonstrate advanced dictionary comprehension techniques"""
    
    print("=== Advanced Dictionary Techniques ===\n")
    
    # Example 1: Dictionary from single list with index
    fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    fruit_index = {fruit: index for index, fruit in enumerate(fruits)}
    
    print("1. Fruit Index Dictionary:")
    for fruit, index in fruit_index.items():
        print(f"   {fruit}: position {index}")
    print()
    
    # Example 2: Dictionary with string manipulation
    words = ['hello', 'world', 'python', 'programming', 'dictionary']
    word_info = {
        word: {
            'length': len(word),
            'uppercase': word.upper(),
            'vowel_count': sum(1 for char in word.lower() if char in 'aeiou')
        }
        for word in words
    }
    
    print("2. Word Information Dictionary:")
    for word, info in word_info.items():
        print(f"   {word}:")
        print(f"     Length: {info['length']}")
        print(f"     Uppercase: {info['uppercase']}")
        print(f"     Vowel count: {info['vowel_count']}")
    print()
    
    # Example 3: Nested dictionary comprehension
    subjects = ['Math', 'Science', 'English']
    students_nested = ['Alice', 'Bob', 'Charlie']
    
    # Create a nested structure: {student: {subject: random_grade}}
    import random
    random.seed(42)  # For consistent results
    
    grade_book = {
        student: {subject: random.randint(70, 100) for subject in subjects}
        for student in students_nested
    }
    
    print("3. Student Grade Book (Nested Dictionary):")
    for student, grades in grade_book.items():
        print(f"   {student}:")
        for subject, grade in grades.items():
            print(f"     {subject}: {grade}")
        avg_grade = sum(grades.values()) / len(grades)
        print(f"     Average: {avg_grade:.1f}")
    print()
    
    return fruit_index, word_info, grade_book

def interactive_dictionary_builder():
    """Interactive function to build dictionaries from user input"""
    
    print("=== Interactive Dictionary Builder ===")
    
    try:
        # Get keys from user
        keys_input = input("Enter keys separated by commas: ")
        keys = [key.strip() for key in keys_input.split(',')]
        
        # Get values from user
        values_input = input("Enter values separated by commas: ")
        values = [value.strip() for value in values_input.split(',')]
        
        # Check if lengths match
        if len(keys) != len(values):
            print(f"Error: Number of keys ({len(keys)}) doesn't match number of values ({len(values)})")
            return
        
        # Create dictionary
        user_dict = {key: value for key, value in zip(keys, values)}
        
        print(f"\nYour dictionary: {user_dict}")
        print(f"Number of items: {len(user_dict)}")
        
        # Try to convert values to numbers if possible
        numeric_dict = {}
        for key, value in user_dict.items():
            try:
                numeric_dict[key] = float(value)
            except ValueError:
                numeric_dict[key] = value
        
        if numeric_dict != user_dict:
            print(f"With numeric conversion: {numeric_dict}")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Run all demonstrations
    basic_dictionary_creation()
    conditional_dictionary_creation()
    advanced_dictionary_techniques()
    
    # Run interactive builder
    interactive_dictionary_builder()
    
    print("\n=== Lab Task 2 Completed Successfully ===")
