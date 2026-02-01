#!/bin/bash

# 1. Create the project directory and enter it
echo "Setting up Lab 10 Environment..."
mkdir -p csv_parser_lab
cd csv_parser_lab || exit

# 2. Create Sample CSV Data (Task 1.1)
echo "Creating sample_data.csv..."
cat << 'EOF' > sample_data.csv
name,age,salary,department,years_experience
John Smith,28,55000,Engineering,3
Jane Doe,32,62000,Marketing,5
Bob Johnson,45,78000,Engineering,12
Alice Brown,29,48000,HR,2
Charlie Wilson,38,71000,Marketing,8
Diana Davis,26,52000,Engineering,1
Frank Miller,41,85000,Engineering,15
Grace Lee,33,59000,HR,6
EOF

# 3. Create the Python CSV Parser (Tasks 2 - 6 combined)
echo "Creating csv_parser.py..."
cat << 'EOF' > csv_parser.py
#!/usr/bin/env python3
"""
CSV Parser - A command-line tool for parsing and analyzing CSV files
"""

import csv
import argparse
import sys
from typing import List, Dict, Any, Optional

# --- Helper Functions (Task 2) ---

def read_csv_file(filename: str) -> List[Dict[str, Any]]:
    """
    Read CSV file and return list of dictionaries
    """
    try:
        with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            return list(reader)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

def is_numeric(value: str) -> bool:
    """
    Check if a string value can be converted to a number
    """
    try:
        float(value)
        return True
    except ValueError:
        return False

def convert_to_number(value: str) -> float:
    """
    Convert string to number (int or float)
    """
    try:
        # Try integer first
        if '.' not in value:
            return float(int(value))
        return float(value)
    except ValueError:
        return 0.0

# --- Statistical Functions (Task 3) ---

def calculate_statistics(data: List[Dict[str, Any]], column: str) -> Dict[str, float]:
    """
    Calculate average, min, and max for a numerical column
    """
    if not data:
        return {"avg": 0, "min": 0, "max": 0, "count": 0}
    
    # Check if column exists
    if column not in data[0]:
        print(f"Error: Column '{column}' not found in CSV file.")
        available_columns = list(data[0].keys())
        print(f"Available columns: {', '.join(available_columns)}")
        sys.exit(1)
    
    # Extract numerical values from the column
    numerical_values = []
    for row in data:
        value = row[column].strip()
        if is_numeric(value):
            numerical_values.append(convert_to_number(value))
        else:
            print(f"Warning: Non-numeric value '{value}' found in column '{column}', skipping...")
    
    if not numerical_values:
        print(f"Error: No numerical values found in column '{column}'")
        sys.exit(1)
    
    # Calculate statistics
    avg_value = sum(numerical_values) / len(numerical_values)
    min_value = min(numerical_values)
    max_value = max(numerical_values)
    
    return {
        "avg": round(avg_value, 2),
        "min": min_value,
        "max": max_value,
        "count": len(numerical_values)
    }

def display_statistics(stats: Dict[str, float], column: str) -> None:
    """
    Display statistics in a formatted way
    """
    print(f"\nStatistics for column '{column}':")
    print("-" * 40)
    print(f"Average: {stats['avg']}")
    print(f"Minimum: {stats['min']}")
    print(f"Maximum: {stats['max']}")
    print(f"Count: {stats['count']} values")

# --- Filtering Functions (Task 4) ---

def filter_rows(data: List[Dict[str, Any]], filter_column: str, filter_value: str) -> List[Dict[str, Any]]:
    """
    Filter rows based on column value
    """
    if not data:
        return []
    
    # Check if filter column exists
    if filter_column not in data[0]:
        print(f"Error: Filter column '{filter_column}' not found in CSV file.")
        available_columns = list(data[0].keys())
        print(f"Available columns: {', '.join(available_columns)}")
        sys.exit(1)
    
    # Filter rows
    filtered_data = []
    for row in data:
        if row[filter_column].strip().lower() == filter_value.lower():
            filtered_data.append(row)
    
    return filtered_data

def display_filtered_data(data: List[Dict[str, Any]], filter_column: str, filter_value: str) -> None:
    """
    Display filtered data in a formatted table
    """
    if not data:
        print(f"No rows found where {filter_column} = '{filter_value}'")
        return
    
    print(f"\nRows where {filter_column} = '{filter_value}' ({len(data)} found):")
    print("-" * 60)
    
    # Get column headers
    headers = list(data[0].keys())
    
    # Print headers
    header_line = " | ".join(f"{header:15}" for header in headers)
    print(header_line)
    print("-" * len(header_line))
    
    # Print data rows
    for row in data:
        row_line = " | ".join(f"{str(row[header]):15}" for header in headers)
        print(row_line)

# --- Argument Parsing and Main Logic (Tasks 5 & 6) ---

def create_argument_parser() -> argparse.ArgumentParser:
    """
    Create and configure argument parser
    """
    parser = argparse.ArgumentParser(
        description="CSV Parser - Analyze CSV files from command line",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python csv_parser.py data.csv --column salary
  python csv_parser.py data.csv --column age --filter department Engineering
  python csv_parser.py data.csv --column salary --filter name "John Smith"
        """
    )
    
    parser.add_argument(
        'filename',
        help='Path to the CSV file to parse'
    )
    
    parser.add_argument(
        '--column', '-c',
        required=True,
        help='Column name to calculate statistics for (must contain numerical data)'
    )
    
    parser.add_argument(
        '--filter', '-f',
        nargs=2,
        metavar=('COLUMN', 'VALUE'),
        help='Filter rows by column value (format: --filter column_name value)'
    )
    
    parser.add_argument(
        '--show-data', '-s',
        action='store_true',
        help='Show filtered data in addition to statistics'
    )
    
    return parser

def main():
    """
    Main function to execute the CSV parser
    """
    # Parse command line arguments
    parser = create_argument_parser()
    args = parser.parse_args()
    
    # Read CSV file
    print(f"Reading CSV file: {args.filename}")
    data = read_csv_file(args.filename)
    
    if not data:
        print("Error: CSV file is empty or could not be read.")
        sys.exit(1)
    
    print(f"Successfully loaded {len(data)} rows of data.")
    
    # Apply filtering if specified
    if args.filter:
        filter_column, filter_value = args.filter
        print(f"Applying filter: {filter_column} = '{filter_value}'")
        filtered_data = filter_rows(data, filter_column, filter_value)
        
        if args.show_data:
            display_filtered_data(filtered_data, filter_column, filter_value)
        
        # Use filtered data for statistics
        data_for_stats = filtered_data
        
        if not data_for_stats:
            print("No data remaining after filtering. Cannot calculate statistics.")
            sys.exit(1)
    else:
        data_for_stats = data
    
    # Calculate and display statistics
    stats = calculate_statistics(data_for_stats, args.column)
    display_statistics(stats, args.column)
    
    # Show summary
    if args.filter:
        print(f"\nSummary: Analyzed {stats['count']} values from column '{args.column}' "
              f"where {args.filter[0]} = '{args.filter[1]}'")
    else:
        print(f"\nSummary: Analyzed {stats['count']} values from column '{args.column}' "
              f"across all {len(data)} rows")

if __name__ == "__main__":
    main()
EOF

# 4. Make script executable (Task 7.1)
chmod +x csv_parser.py

# 5. Create Extended Dataset (Task 8.1)
echo "Creating employees.csv..."
cat << 'EOF' > employees.csv
employee_id,name,age,salary,department,years_experience,performance_rating
1001,John Smith,28,55000,Engineering,3,4.2
1002,Jane Doe,32,62000,Marketing,5,4.5
1003,Bob Johnson,45,78000,Engineering,12,4.8
1004,Alice Brown,29,48000,HR,2,4.0
1005,Charlie Wilson,38,71000,Marketing,8,4.3
1006,Diana Davis,26,52000,Engineering,1,3.9
1007,Frank Miller,41,85000,Engineering,15,4.9
1008,Grace Lee,33,59000,HR,6,4.4
1009,Tom Anderson,35,67000,Marketing,7,4.1
1010,Sarah Johnson,30,54000,Engineering,4,4.2
1011,Mike Brown,42,79000,Engineering,13,4.7
1012,Lisa Wilson,27,49000,HR,3,4.0
1013,David Miller,39,73000,Marketing,9,4.6
1014,Emma Davis,31,58000,HR,5,4.3
1015,James Lee,36,69000,Marketing,8,4.4
EOF

# 6. Create Usage Examples File (Task 9.2)
echo "Creating usage_examples.txt..."
cat << 'EOF' > usage_examples.txt
CSV Parser Usage Examples
========================

Basic Statistics:
python3 csv_parser.py sample_data.csv --column salary
python3 csv_parser.py employees.csv --column age

Filtered Statistics:
python3 csv_parser.py sample_data.csv --column salary --filter department Engineering
python3 csv_parser.py employees.csv --column performance_rating --filter department Marketing

Show Filtered Data:
python3 csv_parser.py sample_data.csv --column salary --filter department HR --show-data
python3 csv_parser.py employees.csv --column age --filter department Engineering --show-data

Advanced Examples:
python3 csv_parser.py employees.csv --column years_experience --filter department Engineering --show-data
python3 csv_parser.py employees.csv --column salary --filter name "John Smith"
EOF

# 7. Create README
echo "Creating README.md..."
cat << 'EOF' > README.md
# Lab 10: Build a Command-Line CSV Parser

## Objectives
- Create a Python command-line application using the `argparse` module.
- Parse CSV files and extract data from specific columns.
- Calculate statistical measures (average, minimum, maximum).
- Implement filtering functionality to process specific rows.
- Structure code using functions for better organization.

## Files Included
- **csv_parser.py**: The main Python script that contains logic for parsing, filtering, and calculating stats.
- **sample_data.csv**: A small dataset (8 rows) for initial testing.
- **employees.csv**: A larger dataset (15 rows) for advanced testing.
- **usage_examples.txt**: A cheat sheet of commands to try.

## How to Run

1. **Make the script executable:**
   \`\`\`bash
   chmod +x csv_parser.py
   \`\`\`

2. **Basic Usage:**
   \`\`\`bash
   ./csv_parser.py <filename> --column <column_name>
   \`\`\`

3. **With Filtering:**
   \`\`\`bash
   ./csv_parser.py employees.csv --column salary --filter department Engineering
   \`\`\`

4. **Show filtered data rows:**
   \`\`\`bash
   ./csv_parser.py employees.csv --column age --filter department HR --show-data
   \`\`\`

5. **View Help:**
   \`\`\`bash
   ./csv_parser.py --help
   \`\`\`
EOF

echo "Setup complete! All files created in directory: csv_parser_lab"
