#!/usr/bin/env python3
"""
Comprehensive test script for all loop examples
"""

def test_for_loop():
    """Test for loop functionality"""
    print("=== Testing For Loop ===")
    numbers = [5, 10, 15, 20, 25]
    total = 0
    
    for num in numbers:
        total += num
    
    expected = 75
    if total == expected:
        print("✅ For loop test PASSED")
    else:
        print(f"❌ For loop test FAILED: expected {expected}, got {total}")

def test_while_loop():
    """Test while loop functionality"""
    print("\n=== Testing While Loop ===")
    count = 5
    result = []
    
    while count > 0:
        result.append(count)
        count -= 1
    
    expected = [5, 4, 3, 2, 1]
    if result == expected:
        print("✅ While loop test PASSED")
    else:
        print(f"❌ While loop test FAILED: expected {expected}, got {result}")

def test_break_continue():
    """Test break and continue statements"""
    print("\n=== Testing Break and Continue ===")
    
    # Test break
    numbers = [1, 2, 3, 4, 5]
    found_position = -1
    
    for i, num in enumerate(numbers):
        if num == 3:
            found_position = i
            break
    
    if found_position == 2:
        print("✅ Break statement test PASSED")
    else:
        print(f"❌ Break statement test FAILED")
    
    # Test continue
    even_numbers = []
    for num in range(1, 11):
        if num % 2 != 0:
            continue
        even_numbers.append(num)
    
    expected_evens = [2, 4, 6, 8, 10]
    if even_numbers == expected_evens:
        print("✅ Continue statement test PASSED")
    else:
        print(f"❌ Continue statement test FAILED")

def test_nested_loops():
    """Test nested loop functionality"""
    print("\n=== Testing Nested Loops ===")
    
    result = []
    for i in range(1, 4):
        for j in range(1, 4):
            result.append(i * j)
    
    expected = [1, 2, 3, 2, 4, 6, 3, 6, 9]
    if result == expected:
        print("✅ Nested loops test PASSED")
    else:
        print(f"❌ Nested loops test FAILED")

# Run all tests
if __name__ == "__main__":
    print("="*50)
    print("Running Loop Tests")
    print("="*50)
    print()
    
    test_for_loop()
    test_while_loop()
    test_break_continue()
    test_nested_loops()
    
    print("\n" + "="*50)
    print("🎉 All tests completed!")
    print("="*50)
