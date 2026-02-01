# Practice Exercises

# Exercise 1: Temperature Statistics Function
def temperature_statistics(temperatures, scale='C'):
    """
    Calculate statistics for a list of temperatures
    Returns: (min, max, average, count)
    """
    if not temperatures:
        return None, None, None, 0
    
    try:
        # Convert all to floats
        temps = [float(t) for t in temperatures]
        
        min_temp = min(temps)
        max_temp = max(temps)
        avg_temp = sum(temps) / len(temps)
        count = len(temps)
        
        return min_temp, max_temp, avg_temp, count
    
    except ValueError:
        print("Error: Invalid temperature values")
        return None, None, None, 0

# Test Exercise 1
print("=== Exercise 1: Temperature Statistics ===")
temps = [20, 25, 30, 18, 22, 28, 35]
min_temp, max_temp, avg_temp, count = temperature_statistics(temps)

if min_temp is not None:
    print(f"Temperature Data: {temps}")
    print(f"Min: {min_temp}°C")
    print(f"Max: {max_temp}°C")
    print(f"Average: {avg_temp:.1f}°C")
    print(f"Count: {count}")
print()

# Exercise 2: Temperature Range Validator
def validate_temperature_range(temperature, scale, min_safe, max_safe):
    """
    Validate if temperature is within safe operating range
    Returns: (is_valid, warning_message)
    """
    try:
        temperature = float(temperature)
        min_safe = float(min_safe)
        max_safe = float(max_safe)
        
        if temperature < min_safe:
            return False, f"⚠️ Temperature too low! Below {min_safe}°{scale}"
        elif temperature > max_safe:
            return False, f"⚠️ Temperature too high! Above {max_safe}°{scale}"
        else:
            return True, f"✓ Temperature within safe range ({min_safe}°{scale} - {max_safe}°{scale})"
    
    except ValueError:
        return False, "Error: Invalid temperature or range values"

# Test Exercise 2
print("=== Exercise 2: Temperature Range Validator ===")
test_temps = [15, 25, 35, 45]
safe_min = 18
safe_max = 40

for temp in test_temps:
    is_valid, message = validate_temperature_range(temp, 'C', safe_min, safe_max)
    print(f"{temp}°C: {message}")
print()

# Exercise 3: Multi-Unit Converter
def convert_all_units(temperature, from_scale):
    """
    Convert a temperature to all other scales
    Returns: dictionary with all conversions
    """
    from_scale = from_scale.upper()
    
    try:
        temperature = float(temperature)
        
        # Convert to Celsius first
        if from_scale == 'C':
            celsius = temperature
        elif from_scale == 'F':
            celsius = (temperature - 32) * 5/9
        elif from_scale == 'K':
            celsius = temperature - 273.15
        else:
            return None
        
        # Convert to all scales
        conversions = {
            'Celsius': celsius,
            'Fahrenheit': (celsius * 9/5) + 32,
            'Kelvin': celsius + 273.15,
            'Rankine': (celsius + 273.15) * 9/5
        }
        
        return conversions
    
    except ValueError:
        return None

# Test Exercise 3
print("=== Exercise 3: Multi-Unit Converter ===")
test_temp = 100
test_scale = 'C'

results = convert_all_units(test_temp, test_scale)
if results:
    print(f"Converting {test_temp}°{test_scale} to all units:")
    for unit, value in results.items():
        print(f"  {unit}: {value:.2f}°")
