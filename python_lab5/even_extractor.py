#!/usr/bin/env python3
"""
Even Number Extractor using List Comprehensions
This script demonstrates various methods to extract even numbers from lists
"""

def demonstrate_even_extraction():
    """Demonstrate different approaches to extract even numbers"""
    
    # Sample data sets
    small_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    large_numbers = list(range(1, 101))  # Numbers 1 to 100
    mixed_numbers = [15, 22, 33, 44, 55, 66, 77, 88, 99, 100]
    
    print("=== Even Number Extraction Demonstration ===\n")
    
    # Method 1: Basic list comprehension
    print("1. Basic List Comprehension:")
    even_basic = [num for num in small_numbers if num % 2 == 0]
    print(f"   Input: {small_numbers}")
    print(f"   Even numbers: {even_basic}")
    print(f"   Count: {len(even_basic)}\n")
    
    # Method 2: List comprehension with range
    print("2. List Comprehension with Range (1-20):")
    even_range = [num for num in range(1, 21) if num % 2 == 0]
    print(f"   Even numbers: {even_range}")
    print(f"   Count: {len(even_range)}\n")
    
    # Method 3: List comprehension with transformation
    print("3. List Comprehension with Transformation:")
    even_squared = [num**2 for num in small_numbers if num % 2 == 0]
    print(f"   Input: {small_numbers}")
    print(f"   Even numbers squared: {even_squared}")
    print(f"   Count: {len(even_squared)}\n")
    
    # Method 4: Nested conditions
    print("4. Multiple Conditions (Even and > 5):")
    even_greater_five = [num for num in large_numbers if num % 2 == 0 and num > 5]
    print(f"   Even numbers greater than 5 (first 10): {even_greater_five[:10]}")
    print(f"   Total count: {len(even_greater_five)}\n")
    
    # Method 5: String formatting within comprehension
    print("5. String Formatting within Comprehension:")
    even_formatted = [f"Number {num} is even" for num in mixed_numbers if num % 2 == 0]
    for item in even_formatted:
        print(f"   {item}")
    
    return even_basic, even_range, even_squared

def interactive_even_finder():
    """Interactive function to find even numbers from user input"""
    
    print("\n=== Interactive Even Number Finder ===")
    
    try:
        # Get user input
        user_input = input("Enter numbers separated by spaces: ")
        user_numbers = [int(x.strip()) for x in user_input.split()]
        
        # Extract even numbers
        user_evens = [num for num in user_numbers if num % 2 == 0]
        
        print(f"Your input: {user_numbers}")
        print(f"Even numbers found: {user_evens}")
        print(f"Count of even numbers: {len(user_evens)}")
        
        # Calculate percentage
        if user_numbers:
            percentage = (len(user_evens) / len(user_numbers)) * 100
            print(f"Percentage of even numbers: {percentage:.1f}%")
        
    except ValueError:
        print("Error: Please enter valid integers separated by spaces")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Run demonstrations
    demonstrate_even_extraction()
    
    # Run interactive finder
    interactive_even_finder()
    
    print("\n=== Lab Task 1 Completed Successfully ===")
