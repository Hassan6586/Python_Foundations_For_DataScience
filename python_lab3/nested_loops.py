# Nested Loops with Break and Continue

def multiplication_table_generator():
    """
    Generate multiplication tables with loop control
    """
    print("=== Multiplication Table Generator ===")
    
    for table in range(1, 6):  # Tables 1 to 5
        print(f"\n📋 Table for {table}:")
        
        for multiplier in range(1, 11):  # 1 to 10
            # Skip multiplying by 7 (continue example)
            if multiplier == 7:
                print(f"   Skipping {table} × {multiplier}")
                continue
            
            result = table * multiplier
            print(f"   {table} × {multiplier} = {result}")
            
            # Stop table if result exceeds 30 (break example)
            if result > 30:
                print(f"   ⏹️ Stopping table {table} (result exceeded 30)")
                break
        
        # Ask user if they want to continue to next table
        if table < 5:  # Don't ask after the last table
            continue_choice = input("\nContinue to next table? (y/n): ").lower()
            if continue_choice != 'y':
                print("👋 Stopping table generation...")
                break

# Run the generator
multiplication_table_generator()
