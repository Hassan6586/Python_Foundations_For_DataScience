# Interactive Temperature Converter

def display_menu():
    """Display the conversion menu"""
    print("\n" + "="*40)
    print("    TEMPERATURE CONVERTER MENU")
    print("="*40)
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Batch convert")
    print("6. Exit")
    print("="*40)

def get_temperature_input(scale):
    """Get temperature input from user with validation"""
    while True:
        try:
            temp = float(input(f"Enter temperature in {scale}: "))
            return temp
        except ValueError:
            print("Please enter a valid number!")

def convert_temperature(temp, conversion_type):
    """Perform temperature conversion based on type"""
    conversions = {
        1: lambda x: ((x * 9/5) + 32, f"{x}°C = {(x * 9/5) + 32:.2f}°F"),
        2: lambda x: ((x - 32) * 5/9, f"{x}°F = {(x - 32) * 5/9:.2f}°C"),
        3: lambda x: (x + 273.15, f"{x}°C = {x + 273.15:.2f}K"),
        4: lambda x: (x - 273.15, f"{x}K = {x - 273.15:.2f}°C")
    }
    
    if conversion_type in conversions:
        result, message = conversions[conversion_type](temp)
        return result, message
    else:
        return None, "Invalid conversion type"

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * 5/9

def process_temperature_list(temperatures, conversion_type):
    """Process a list of temperatures"""
    converted_temps = []
    
    for temp in temperatures:
        try:
            temp = float(temp)
            
            if conversion_type == 'c_to_f':
                converted = celsius_to_fahrenheit(temp)
                converted_temps.append((temp, converted, 'C', 'F'))
            elif conversion_type == 'f_to_c':
                converted = fahrenheit_to_celsius(temp)
                converted_temps.append((temp, converted, 'F', 'C'))
                
        except ValueError:
            print(f"Skipping invalid temperature: {temp}")
    
    return converted_temps

def batch_convert_from_input():
    """Handle batch conversion from user input"""
    print("\nBatch Conversion Mode")
    print("Enter temperatures separated by commas (e.g., 0, 25, 100)")
    
    temp_input = input("Enter temperatures: ")
    temp_list = [t.strip() for t in temp_input.split(',')]
    
    print("Select conversion type:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    
    try:
        conv_choice = int(input("Choice (1-2): "))
        if conv_choice == 1:
            results = process_temperature_list(temp_list, 'c_to_f')
        elif conv_choice == 2:
            results = process_temperature_list(temp_list, 'f_to_c')
        else:
            print("Invalid choice!")
            return
        
        print("\nBatch Conversion Results:")
        for original, converted, from_unit, to_unit in results:
            print(f"{original}°{from_unit} → {converted:.2f}°{to_unit}")
            
    except ValueError:
        print("Invalid input!")

def main_converter_loop():
    """Main program loop"""
    print("Welcome to the Advanced Temperature Converter!")
    
    while True:
        display_menu()
        
        try:
            choice = int(input("Select an option (1-6): "))
            
            if choice == 6:
                print("Thank you for using the Temperature Converter!")
                break
            elif choice in [1, 2, 3, 4]:
                scale_names = {1: "Celsius", 2: "Fahrenheit", 3: "Celsius", 4: "Kelvin"}
                temp = get_temperature_input(scale_names[choice])
                
                result, message = convert_temperature(temp, choice)
                if result is not None:
                    print(f"\nResult: {message}")
                else:
                    print(f"Error: {message}")
                    
            elif choice == 5:
                batch_convert_from_input()
            else:
                print("Invalid choice! Please select 1-6.")
                
        except ValueError:
            print("Please enter a valid number!")
        
        input("\nPress Enter to continue...")

# Run the main program
if __name__ == "__main__":
    main_converter_loop()
