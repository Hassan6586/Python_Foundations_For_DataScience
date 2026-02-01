# Advanced Temperature Converter - Multiple Return Values

def convert_from_celsius(celsius):
    """
    Convert Celsius to multiple temperature scales
    Returns: (fahrenheit, kelvin, rankine, status)
    """
    try:
        celsius = float(celsius)
        
        # Validate input
        if celsius < -273.15:
            return None, None, None, "Temperature below absolute zero"
        
        # Convert to different scales
        fahrenheit = (celsius * 9/5) + 32
        kelvin = celsius + 273.15
        rankine = (celsius + 273.15) * 9/5
        
        return fahrenheit, kelvin, rankine, "Success"
    
    except ValueError:
        return None, None, None, "Invalid input: not a number"

# Test the function
print("=== Multi-Scale Temperature Converter ===")
celsius_temp = 100

fahrenheit, kelvin, rankine, status = convert_from_celsius(celsius_temp)

if status == "Success":
    print(f"Temperature Conversions for {celsius_temp}°C:")
    print(f"Fahrenheit: {fahrenheit}°F")
    print(f"Kelvin: {kelvin}K")
    print(f"Rankine: {rankine}°R")
else:
    print(f"Error: {status}")

print()

# Universal temperature converter
def universal_temperature_converter(temperature, from_scale, to_scale):
    """
    Convert temperature between different scales
    Supported scales: 'C' (Celsius), 'F' (Fahrenheit), 'K' (Kelvin)
    Returns: (converted_temperature, status_message)
    """
    try:
        temperature = float(temperature)
        from_scale = from_scale.upper()
        to_scale = to_scale.upper()
        
        # First convert everything to Celsius
        if from_scale == 'C':
            celsius = temperature
        elif from_scale == 'F':
            celsius = (temperature - 32) * 5/9
        elif from_scale == 'K':
            celsius = temperature - 273.15
        else:
            return None, f"Unsupported scale: {from_scale}"
        
        # Validate celsius is above absolute zero
        if celsius < -273.15:
            return None, "Temperature below absolute zero"
        
        # Convert from Celsius to target scale
        if to_scale == 'C':
            result = celsius
        elif to_scale == 'F':
            result = (celsius * 9/5) + 32
        elif to_scale == 'K':
            result = celsius + 273.15
        else:
            return None, f"Unsupported scale: {to_scale}"
        
        return result, "Success"
    
    except ValueError:
        return None, "Invalid temperature value"

# Test the universal converter
print("=== Universal Temperature Converter ===")
test_conversions = [
    (32, 'F', 'C'),
    (0, 'C', 'K'),
    (273.15, 'K', 'F'),
    (100, 'C', 'F')
]

for temp, from_s, to_s in test_conversions:
    result, status = universal_temperature_converter(temp, from_s, to_s)
    if status == "Success":
        print(f"{temp}°{from_s} = {result:.2f}°{to_s}")
    else:
        print(f"Error converting {temp}°{from_s} to °{to_s}: {status}")
