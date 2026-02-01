# Sum numbers in a list using for loop

# Part 1: Basic for loop example
print("=== Part 1: Basic For Loop ===")
numbers = [1, 2, 3, 4, 5]

print("Numbers in the list:")
for number in numbers:
    print(number)

print()

# Part 2: Sum calculation
print("=== Part 2: Sum Calculation ===")
numbers = [10, 25, 30, 45, 50]

# Initialize sum variable
total_sum = 0

print("Numbers in the list:", numbers)
print("Calculating sum...")

# Loop through each number and add to total
for number in numbers:
    total_sum = total_sum + number
    print(f"Adding {number}, current sum: {total_sum}")

print(f"Final sum: {total_sum}")
print()

# Part 3: Interactive sum calculator
print("=== Part 3: Interactive Sum Calculator ===")

def calculate_sum():
    numbers = []
    
    print("Enter numbers to sum (type 'done' when finished):")
    
    while True:
        user_input = input("Enter a number: ")
        
        if user_input.lower() == 'done':
            break
            
        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("Please enter a valid number or 'done' to finish.")
    
    if not numbers:
        print("No numbers entered.")
        return
    
    # Calculate sum using for loop
    total_sum = 0
    print("\nCalculating sum:")
    
    for number in numbers:
        total_sum += number
        print(f"Adding {number}, running total: {total_sum}")
    
    print(f"\nFinal sum of {len(numbers)} numbers: {total_sum}")
    print(f"Average: {total_sum / len(numbers):.2f}")

# Run the calculator
calculate_sum()
