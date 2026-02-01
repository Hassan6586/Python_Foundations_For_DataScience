#!/bin/bash

# 1. Create the main directory and enter it
echo "Setting up Lab 9 Environment..."
mkdir -p lab9_weather_api
cd lab9_weather_api || exit

# 2. Install required libraries (Task 2)
echo "Installing required Python libraries..."
pip install requests tabulate

# 3. Create Test Imports Script (Task 2.3)
echo "Creating test_imports.py..."
cat << 'EOF' > test_imports.py
import requests
import json
from tabulate import tabulate

print("All libraries imported successfully!")
print("Requests version:", requests.__version__)
EOF

# 4. Create Intermediate Weather Retriever Script (Tasks 3-6)
# This combines the code from Tasks 3, 4, 5, and 6 into a functional script.
echo "Creating weather_retriever.py..."
cat << 'EOF' > weather_retriever.py
import requests
import json
from tabulate import tabulate
import sys
from datetime import datetime

# API Configuration
API_KEY = "YOUR_API_KEY_HERE"  # Replace with your actual API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather_data(city_name):
    """
    Fetch weather data for a given city
    """
    try:
        # Construct the API URL
        url = f"{BASE_URL}?q={city_name}&appid={API_KEY}&units=metric"
        
        # Make the HTTP request
        response = requests.get(url)
        
        # Check if request was successful
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: Unable to fetch data for {city_name}")
            print(f"Status code: {response.status_code}")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"JSON parsing error: {e}")
        return None

def extract_weather_info(weather_data):
    """
    Extract relevant weather information from API response
    """
    if not weather_data:
        return None
    
    try:
        extracted_info = {
            'City': weather_data['name'],
            'Country': weather_data['sys']['country'],
            'Temperature (°C)': weather_data['main']['temp'],
            'Feels Like (°C)': weather_data['main']['feels_like'],
            'Humidity (%)': weather_data['main']['humidity'],
            'Pressure (hPa)': weather_data['main']['pressure'],
            'Weather': weather_data['weather'][0]['description'].title(),
            'Wind Speed (m/s)': weather_data['wind']['speed'],
            'Visibility (m)': weather_data.get('visibility', 'N/A'),
            'Timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        return extracted_info
        
    except KeyError as e:
        print(f"Error extracting data: Missing key {e}")
        return None

def get_multiple_cities_weather(cities):
    """
    Get weather data for multiple cities
    """
    weather_results = []
    
    for city in cities:
        print(f"Fetching weather data for {city}...")
        raw_data = get_weather_data(city)
        extracted_data = extract_weather_info(raw_data)
        
        if extracted_data:
            weather_results.append(extracted_data)
        else:
            print(f"Failed to get data for {city}")
    
    return weather_results

def display_weather_table(weather_data_list):
    """
    Display weather data in a formatted table
    """
    if not weather_data_list:
        print("No weather data to display.")
        return
    
    # Create headers from the first data entry
    headers = list(weather_data_list[0].keys())
    
    # Create rows for the table
    rows = []
    for data in weather_data_list:
        rows.append(list(data.values()))
    
    # Display the table
    print("\n" + "="*80)
    print("WEATHER DATA SUMMARY")
    print("="*80)
    print(tabulate(rows, headers=headers, tablefmt="grid"))
    print("="*80)

def display_weather_summary(weather_data_list):
    """
    Display summary statistics of weather data
    """
    if not weather_data_list:
        return
    
    temperatures = [data['Temperature (°C)'] for data in weather_data_list]
    humidity_levels = [data['Humidity (%)'] for data in weather_data_list]
    
    summary_data = [
        ['Total Cities', len(weather_data_list)],
        ['Average Temperature (°C)', f"{sum(temperatures)/len(temperatures):.1f}"],
        ['Highest Temperature (°C)', f"{max(temperatures):.1f}"],
        ['Lowest Temperature (°C)', f"{min(temperatures):.1f}"],
        ['Average Humidity (%)', f"{sum(humidity_levels)/len(humidity_levels):.1f}"]
    ]
    
    print("\nWEATHER SUMMARY STATISTICS")
    print("-" * 40)
    print(tabulate(summary_data, headers=['Metric', 'Value'], tablefmt="simple"))

def main():
    """
    Main program function
    """
    print("Weather Data Retrieval System")
    print("=" * 40)
    
    # Check if API key is set
    if API_KEY == "YOUR_API_KEY_HERE":
        print("Error: Please set your API key in the script!")
        print("Get your API key from: https://openweathermap.org/api")
        sys.exit(1)
    
    # Option 1: Single city
    print("\nOption 1: Single City Weather")
    city = input("Enter city name (or press Enter to skip): ").strip()
    
    if city:
        weather_data = get_weather_data(city)
        extracted_data = extract_weather_info(weather_data)
        
        if extracted_data:
            display_weather_table([extracted_data])
    
    # Option 2: Multiple cities
    print("\nOption 2: Multiple Cities Weather")
    cities_input = input("Enter city names separated by commas (or press Enter to use defaults): ").strip()
    
    if cities_input:
        cities = [city.strip() for city in cities_input.split(',')]
    else:
        # Default cities for demonstration
        cities = ['London', 'New York', 'Tokyo', 'Sydney', 'Paris']
        print(f"Using default cities: {', '.join(cities)}")
    
    # Get weather data for multiple cities
    weather_results = get_multiple_cities_weather(cities)
    
    if weather_results:
        display_weather_table(weather_results)
        display_weather_summary(weather_results)
    else:
        print("No weather data retrieved.")

if __name__ == "__main__":
    main()
EOF

# 5. Create Final Enhanced Script (Task 10)
echo "Creating weather_app_final.py..."
cat << 'EOF' > weather_app_final.py
#!/usr/bin/env python3
"""
Weather Data Retrieval System
Automated weather data fetching using OpenWeatherMap API
"""

import requests
import json
from tabulate import tabulate
import sys
from datetime import datetime
import re

# API Configuration
API_KEY = "YOUR_API_KEY_HERE"  # Replace with your actual API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def validate_city_name(city_name):
    """Validate city name input"""
    if not city_name or not city_name.strip():
        return False
    pattern = r'^[a-zA-Z\s\-]+$'
    return bool(re.match(pattern, city_name.strip()))

def get_weather_data(city_name):
    """Fetch weather data for a given city with error handling"""
    if not validate_city_name(city_name):
        print(f"Invalid city name: {city_name}")
        return None
    
    try:
        url = f"{BASE_URL}?q={city_name}&appid={API_KEY}&units=metric"
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            print(f"City not found: {city_name}")
        elif response.status_code == 401:
            print("Invalid API key. Please check your API key.")
        else:
            print(f"API error for {city_name}: Status {response.status_code}")
        
        return None
        
    except requests.exceptions.Timeout:
        print(f"Timeout error for {city_name}")
        return None
    except requests.exceptions.ConnectionError:
        print(f"Connection error for {city_name}")
        return None
    except Exception as e:
        print(f"Unexpected error for {city_name}: {e}")
        return None

def extract_weather_info(weather_data):
    """Extract relevant weather information from API response"""
    if not weather_data:
        return None
    
    try:
        extracted_info = {
            'City': weather_data['name'],
            'Country': weather_data['sys']['country'],
            'Temperature (°C)': weather_data['main']['temp'],
            'Feels Like (°C)': weather_data['main']['feels_like'],
            'Humidity (%)': weather_data['main']['humidity'],
            'Pressure (hPa)': weather_data['main']['pressure'],
            'Weather': weather_data['weather'][0]['description'].title(),
            'Wind Speed (m/s)': weather_data['wind']['speed'],
            'Visibility (m)': weather_data.get('visibility', 'N/A'),
            'Timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        return extracted_info
        
    except KeyError as e:
        print(f"Error extracting data: Missing key {e}")
        return None

def display_weather_table(weather_data_list):
    """Display weather data in a formatted table"""
    if not weather_data_list:
        print("No weather data to display.")
        return
    
    headers = list(weather_data_list[0].keys())
    rows = [list(data.values()) for data in weather_data_list]
    
    print("\n" + "="*80)
    print("WEATHER DATA SUMMARY")
    print("="*80)
    print(tabulate(rows, headers=headers, tablefmt="grid"))
    print("="*80)

def display_weather_summary(weather_data_list):
    """Display summary statistics of weather data"""
    if not weather_data_list:
        return
    
    temperatures = [data['Temperature (°C)'] for data in weather_data_list]
    humidity_levels = [data['Humidity (%)'] for data in weather_data_list]
    
    summary_data = [
        ['Total Cities', len(weather_data_list)],
        ['Average Temperature (°C)', f"{sum(temperatures)/len(temperatures):.1f}"],
        ['Highest Temperature (°C)', f"{max(temperatures):.1f}"],
        ['Lowest Temperature (°C)', f"{min(temperatures):.1f}"],
        ['Average Humidity (%)', f"{sum(humidity_levels)/len(humidity_levels):.1f}"]
    ]
    
    print("\nWEATHER SUMMARY STATISTICS")
    print("-" * 40)
    print(tabulate(summary_data, headers=['Metric', 'Value'], tablefmt="simple"))

def main():
    """Main program function"""
    print("Weather Data Retrieval System")
    print("=" * 40)
    
    if API_KEY == "YOUR_API_KEY_HERE":
        print("Error: Please set your API key in the script!")
        print("Get your API key from: https://openweathermap.org/api")
        sys.exit(1)
    
    # Get cities from user input
    cities_input = input("Enter city names separated by commas: ").strip()
    
    if cities_input:
        cities = [city.strip() for city in cities_input.split(',')]
    else:
        cities = ['London', 'New York', 'Tokyo', 'Sydney', 'Paris']
        print(f"Using default cities: {', '.join(cities)}")
    
    # Fetch weather data
    weather_results = []
    for city in cities:
        print(f"Fetching weather data for {city}...")
        raw_data = get_weather_data(city)
        extracted_data = extract_weather_info(raw_data)
        
        if extracted_data:
            weather_results.append(extracted_data)
    
    # Display results
    if weather_results:
        display_weather_table(weather_results)
        display_weather_summary(weather_results)
    else:
        print("No weather data retrieved.")

if __name__ == "__main__":
    main()
EOF

# 6. Make final script executable
chmod +x weather_app_final.py

# 7. Create README
echo "Creating README.md..."
cat << 'EOF' > README.md
# Lab 9: Automate Weather Data Retrieval with API

## Objectives
- Understand REST APIs and HTTP requests.
- Fetch real-time weather data using OpenWeatherMap API.
- Parse JSON responses and display tabular data.

## Important Note
You must sign up at [OpenWeatherMap](https://openweathermap.org/api) to get a free API Key. 
Once you have the key, open `weather_app_final.py` (or `weather_retriever.py`) and replace:
`API_KEY = "YOUR_API_KEY_HERE"`
with your actual key.

## Files Included
- **test_imports.py**: Verifies that `requests` and `tabulate` libraries are installed.
- **weather_retriever.py**: The intermediate script built during Tasks 3-6.
- **weather_app_final.py**: The complete, enhanced script with error handling and validation (Task 10).

## How to Run
1. Verify setup: \`python3 test_imports.py\`
2. Edit the script to add your API Key: \`nano weather_app_final.py\`
3. Run the application: \`python3 weather_app_final.py\`
EOF

echo "Setup complete! All files created in directory: lab9_weather_api"
echo "IMPORTANT: Don't forget to edit the Python files and insert your OpenWeatherMap API Key."
