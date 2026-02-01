# Loop Control - Break and Continue Examples

# Part 1: Break statement example
print("=== Part 1: Break Statement ===")
numbers = [1, 3, 7, 12, 8, 15, 20, 9]
target = 12

print("Searching for number:", target)
print("Numbers checked:")

for number in numbers:
    print(f"Checking: {number}")
    
    if number == target:
        print(f"✅ Found {target}!")
        break
    
    print(f"❌ {number} is not the target")

print("Search completed")
print()

# Part 2: Continue statement example
print("=== Part 2: Continue Statement ===")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Processing only even numbers:")
even_sum = 0

for number in numbers:
    if number % 2 != 0:  # If number is odd
        print(f"Skipping odd number: {number}")
        continue
    
    # This code only runs for even numbers
    even_sum += number
    print(f"Processing even number: {number}, running sum: {even_sum}")

print(f"Sum of even numbers: {even_sum}")
print()

# Part 3: Data validation system combining break and continue
print("=== Part 3: Data Validation System ===")

def data_validator():
    """
    A data validation system that demonstrates break and continue
    """
    print("Enter numbers (1-100). Type 'quit' to exit, 'skip' to skip invalid entries.")
    
    valid_numbers = []
    total_attempts = 0
    
    while True:
        total_attempts += 1
        
        # Break condition - maximum attempts
        if total_attempts > 20:
            print("⚠️ Maximum attempts reached. Stopping input.")
            break
        
        user_input = input(f"Attempt {total_attempts} - Enter a number: ").strip()
        
        # Break condition - user wants to quit
        if user_input.lower() == 'quit':
            print("👋 Exiting data entry...")
            break
        
        # Continue condition - user wants to skip
        if user_input.lower() == 'skip':
            print("⏭️ Skipping this entry...")
            continue
        
        try:
            number = float(user_input)
            
            # Continue condition - number out of range
            if number < 1 or number > 100:
                print(f"❌ {number} is out of range (1-100). Try again.")
                continue
            
            # Valid number - add to list
            valid_numbers.append(number)
            print(f"✅ Added {number} to the list")
            
            # Display current statistics
            if valid_numbers:
                avg = sum(valid_numbers) / len(valid_numbers)
                print(f"📊 Current stats: {len(valid_numbers)} numbers, average: {avg:.2f}")
        
        except ValueError:
            print("❌ Invalid input. Please enter a number.")
            continue
    
    # Final results
    print("\n=== Final Results ===")
    if valid_numbers:
        print(f"Valid numbers entered: {valid_numbers}")
        print(f"Total count: {len(valid_numbers)}")
        print(f"Sum: {sum(valid_numbers)}")
        print(f"Average: {sum(valid_numbers) / len(valid_numbers):.2f}")
        print(f"Min: {min(valid_numbers)}")
        print(f"Max: {max(valid_numbers)}")
    else:
        print("No valid numbers were entered.")

# Run the validator
data_validator()
