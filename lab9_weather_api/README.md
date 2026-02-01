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
