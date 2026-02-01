# Batch Temperature Processor - Functions in Loops

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * 5/9

def process_temperature_list(temperatures, conversion_type):
    """
    Process a list of temperatures using the specified conversion
    conversion_type: 'c_to_f' or 'f_to_c'
    Returns: list of converted temperatures
    """
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
            else:
                print(f"Unknown conversion type: {conversion_type}")
                
        except ValueError:
            print(f"Skipping invalid temperature: {temp}")
    
    return converted_temps

# Test data
celsius_temperatures = [0, 25, 37, 100, -10, 50]
fahrenheit_temperatures = [32, 77, 98.6, 212, 14, 122]

print("=== Celsius to Fahrenheit Conversions ===")
c_to_f_results = process_temperature_list(celsius_temperatures, 'c_to_f')

for original, converted, from_unit, to_unit in c_to_f_results:
    print(f"{original}°{from_unit} → {converted:.2f}°{to_unit}")

print("\n=== Fahrenheit to Celsius Conversions ===")
f_to_c_results = process_temperature_list(fahrenheit_temperatures, 'f_to_c')

for original, converted, from_unit, to_unit in f_to_c_results:
    print(f"{original}°{from_unit} → {converted:.2f}°{to_unit}")
