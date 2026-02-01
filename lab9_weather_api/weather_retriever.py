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
