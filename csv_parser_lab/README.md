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
