# Best Practices - Documentation and Error Handling

import datetime

def temperature_converter_with_logging(temperature, from_scale, to_scale, log_file=None):
    """
    Advanced temperature converter with logging capabilities
    
    Args:
        temperature (float): Temperature value to convert
        from_scale (str): Source temperature scale ('C', 'F', 'K')
        to_scale (str): Target temperature scale ('C', 'F', 'K')
        log_file (str, optional): Path to log file for recording conversions
    
    Returns:
        tuple: (converted_temperature, success_status, error_message)
    
    Example:
        >>> result, success, error = temperature_converter_with_logging(25, 'C', 'F')
        >>> print(f"25°C = {result}°F")
    """
    try:
        # Input validation
        temperature = float(temperature)
        from_scale = from_scale.upper().strip()
        to_scale = to_scale.upper().strip()
        
        valid_scales = ['C', 'F', 'K']
        if from_scale not in valid_scales or to_scale not in valid_scales:
            return None, False, f"Invalid scale. Use: {', '.join(valid_scales)}"
        
        # Conversion logic
        # Step 1: Convert to Celsius
        if from_scale == 'C':
            celsius = temperature
        elif from_scale == 'F':
            celsius = (temperature - 32) * 5/9
        elif from_scale == 'K':
            celsius = temperature - 273.15
        
        # Validate physical limits
        if celsius < -273.15:
            return None, False, "Temperature below absolute zero (-273.15°C)"
        
        # Step 2: Convert from Celsius to target
        if to_scale == 'C':
            result = celsius
        elif to_scale == 'F':
            result = (celsius * 9/5) + 32
        elif to_scale == 'K':
            result = celsius + 273.15
        
        # Log the conversion if log file is specified
        if log_file:
            log_conversion(temperature, from_scale, result, to_scale, log_file)
        
        return round(result, 2), True, "Conversion successful"
    
    except ValueError:
        return None, False, "Invalid temperature value - must be a number"
    except Exception as e:
        return None, False, f"Unexpected error: {str(e)}"

def log_conversion(original_temp, from_scale, converted_temp, to_scale, log_file):
    """Log temperature conversion to file"""
    try:
        with open(log_file, 'a') as f:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_entry = f"{timestamp} - {original_temp}°{from_scale} → {converted_temp}°{to_scale}\n"
            f.write(log_entry)
    except Exception as e:
        print(f"Logging error: {e}")

# Test the advanced function
print("=== Advanced Temperature Converter Tests ===")
test_cases = [
    (25, 'C', 'F'),
    (32, 'F', 'C'),
    (273.15, 'K', 'C'),
    (-300, 'C', 'F'),  # Should fail - below absolute zero
    ('abc', 'C', 'F'),  # Should fail - invalid input
]

for temp, from_s, to_s in test_cases:
    result, success, message = temperature_converter_with_logging(
        temp, from_s, to_s, 'conversion_log.txt'
    )
    
    if success:
        print(f"✓ {temp}°{from_s} = {result}°{to_s}")
    else:
        print(f"✗ Error converting {temp}°{from_s} to °{to_s}: {message}")

print()

# Performance benchmark
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * 9/5) + 32

def benchmark_conversion_methods():
    """Compare performance of different conversion approaches"""
    import time
    
    # Method 1: Direct calculation
    def direct_conversion(temps):
        results = []
        for temp in temps:
            fahrenheit = (temp * 9/5) + 32
            results.append(fahrenheit)
        return results
    
    # Method 2: Using function calls
    def function_conversion(temps):
        results = []
        for temp in temps:
            fahrenheit = celsius_to_fahrenheit(temp)
            results.append(fahrenheit)
        return results
    
    # Method 3: List comprehension with function
    def comprehension_conversion(temps):
        return [celsius_to_fahrenheit(temp) for temp in temps]
    
    # Test data
    test_temperatures = list(range(-50, 151))  # -50°C to 150°C
    
    methods = [
        ("Direct Calculation", direct_conversion),
        ("Function Calls", function_conversion),
        ("List Comprehension", comprehension_conversion)
    ]
    
    print("=== Performance Benchmark ===")
    for name, method in methods:
        start_time = time.time()
        results = method(test_temperatures)
        end_time = time.time()
        
        print(f"{name}: {end_time - start_time:.6f} seconds")
        print(f"  Processed {len(results)} temperatures")

# Run the benchmark
benchmark_conversion_methods()
