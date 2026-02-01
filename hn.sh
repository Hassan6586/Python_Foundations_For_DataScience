#!/bin/bash

# 1. Create the main directory and enter it
echo "Setting up Lab 6 Environment..."
mkdir -p lab6_file_handling
cd lab6_file_handling || exit

# 2. Create the Sample Text File (Task 1.1)
echo "Creating students.txt..."
cat << 'EOF' > students.txt
John Smith - Computer Science - Grade: A
Sarah Johnson - Mathematics - Grade: B+
Mike Davis - Physics - Grade: A-
Emily Brown - Chemistry - Grade: B
David Wilson - Biology - Grade: A
Lisa Garcia - Engineering - Grade: B+
EOF

# 3. Create the Read Text File Script (Task 1.2)
echo "Creating read_text_file.py..."
cat << 'EOF' > read_text_file.py
#!/usr/bin/env python3

def read_student_file(filename):
    """
    Read student information from a text file line by line
    """
    try:
        # Open the file in read mode
        with open(filename, 'r') as file:
            print("Reading student information:")
            print("-" * 40)
            
            line_number = 1
            for line in file:
                # Remove whitespace and newline characters
                clean_line = line.strip()
                
                if clean_line:  # Skip empty lines
                    print(f"Line {line_number}: {clean_line}")
                    
                    # Parse the line to extract information
                    parts = clean_line.split(' - ')
                    if len(parts) == 3:
                        name = parts[0]
                        subject = parts[1]
                        grade = parts[2].replace('Grade: ', '')
                        
                        print(f"  Name: {name}")
                        print(f"  Subject: {subject}")
                        print(f"  Grade: {grade}")
                        print()
                    
                    line_number += 1
                    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"Error reading file: {e}")

def main():
    filename = "students.txt"
    read_student_file(filename)

if __name__ == "__main__":
    main()
EOF

# 4. Create the Enhanced Text Processor (Task 1.3)
echo "Creating process_text_file.py..."
cat << 'EOF' > process_text_file.py
#!/usr/bin/env python3

def process_student_data(filename):
    """
    Process student data and calculate statistics
    """
    students = []
    subjects = {}
    grades = []
    
    try:
        with open(filename, 'r') as file:
            for line in file:
                clean_line = line.strip()
                if clean_line:
                    parts = clean_line.split(' - ')
                    if len(parts) == 3:
                        name = parts[0]
                        subject = parts[1]
                        grade_str = parts[2].replace('Grade: ', '')
                        
                        # Store student information
                        student_info = {
                            'name': name,
                            'subject': subject,
                            'grade': grade_str
                        }
                        students.append(student_info)
                        
                        # Count subjects
                        if subject in subjects:
                            subjects[subject] += 1
                        else:
                            subjects[subject] = 1
                        
                        # Convert grades to numerical values for statistics
                        grade_value = convert_grade_to_number(grade_str)
                        if grade_value is not None:
                            grades.append(grade_value)
        
        # Display results
        print(f"Total students: {len(students)}")
        print("\nSubject distribution:")
        for subject, count in subjects.items():
            print(f"  {subject}: {count} students")
        
        if grades:
            avg_grade = sum(grades) / len(grades)
            print(f"\nAverage grade (numerical): {avg_grade:.2f}")
            print(f"Highest grade: {max(grades)}")
            print(f"Lowest grade: {min(grades)}")
        
        return students, subjects, grades
        
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return [], {}, []
    except Exception as e:
        print(f"Error processing file: {e}")
        return [], {}, []

def convert_grade_to_number(grade_str):
    """
    Convert letter grades to numerical values
    """
    grade_map = {
        'A': 4.0, 'A-': 3.7,
        'B+': 3.3, 'B': 3.0, 'B-': 2.7,
        'C+': 2.3, 'C': 2.0, 'C-': 1.7,
        'D+': 1.3, 'D': 1.0,
        'F': 0.0
    }
    return grade_map.get(grade_str, None)

def main():
    filename = "students.txt"
    students, subjects, grades = process_student_data(filename)

if __name__ == "__main__":
    main()
EOF

# 5. Create Sample CSV File (Task 2.1)
echo "Creating sales_data.csv..."
cat << 'EOF' > sales_data.csv
Date,Product,Category,Quantity,Price,Sales_Rep
2024-01-15,Laptop,Electronics,2,999.99,John Smith
2024-01-16,Mouse,Electronics,5,25.50,Sarah Johnson
2024-01-17,Keyboard,Electronics,3,75.00,John Smith
2024-01-18,Monitor,Electronics,1,299.99,Mike Davis
2024-01-19,Tablet,Electronics,4,399.99,Sarah Johnson
2024-01-20,Headphones,Electronics,6,89.99,Emily Brown
2024-01-21,Smartphone,Electronics,2,699.99,John Smith
2024-01-22,Charger,Electronics,8,19.99,Mike Davis
2024-01-23,Speaker,Electronics,3,149.99,Sarah Johnson
2024-01-24,Webcam,Electronics,2,79.99,Emily Brown
EOF

# 6. Create CSV Reader Script (Task 2.2)
echo "Creating read_csv_file.py..."
cat << 'EOF' > read_csv_file.py
#!/usr/bin/env python3
import csv
from datetime import datetime

def read_sales_data(filename):
    """
    Read sales data from CSV file using csv module
    """
    sales_data = []
    
    try:
        with open(filename, 'r', newline='') as csvfile:
            # Create CSV reader object
            csv_reader = csv.DictReader(csvfile)
            
            print("Sales Data:")
            print("-" * 80)
            print(f"{'Date':<12} {'Product':<12} {'Quantity':<8} {'Price':<8} {'Sales Rep':<15}")
            print("-" * 80)
            
            for row in csv_reader:
                # Process each row
                date = row['Date']
                product = row['Product']
                quantity = int(row['Quantity'])
                price = float(row['Price'])
                sales_rep = row['Sales_Rep']
                
                # Calculate total for this sale
                total = quantity * price
                
                # Store the data
                sale_record = {
                    'date': date,
                    'product': product,
                    'category': row['Category'],
                    'quantity': quantity,
                    'price': price,
                    'total': total,
                    'sales_rep': sales_rep
                }
                sales_data.append(sale_record)
                
                # Display the data
                print(f"{date:<12} {product:<12} {quantity:<8} ${price:<7.2f} {sales_rep:<15}")
            
            print("-" * 80)
            print(f"Total records processed: {len(sales_data)}")
            
        return sales_data
        
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return []

def main():
    filename = "sales_data.csv"
    sales_data = read_sales_data(filename)

if __name__ == "__main__":
    main()
EOF

# 7. Create Statistics Script (Task 2.3)
echo "Creating calculate_statistics.py..."
cat << 'EOF' > calculate_statistics.py
#!/usr/bin/env python3
import csv
from collections import defaultdict

def calculate_sales_statistics(filename):
    """
    Calculate comprehensive statistics from sales data
    """
    sales_data = []
    
    # Read the CSV file
    try:
        with open(filename, 'r', newline='') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            
            for row in csv_reader:
                quantity = int(row['Quantity'])
                price = float(row['Price'])
                total = quantity * price
                
                sale_record = {
                    'date': row['Date'],
                    'product': row['Product'],
                    'category': row['Category'],
                    'quantity': quantity,
                    'price': price,
                    'total': total,
                    'sales_rep': row['Sales_Rep']
                }
                sales_data.append(sale_record)
                
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None
    
    # Calculate statistics
    if not sales_data:
        print("No data to process.")
        return None
    
    # Basic statistics
    total_sales = sum(record['total'] for record in sales_data)
    total_quantity = sum(record['quantity'] for record in sales_data)
    average_sale = total_sales / len(sales_data)
    
    # Sales by representative
    sales_by_rep = defaultdict(float)
    quantity_by_rep = defaultdict(int)
    
    # Sales by product
    sales_by_product = defaultdict(float)
    quantity_by_product = defaultdict(int)
    
    # Process data for detailed statistics
    for record in sales_data:
        rep = record['sales_rep']
        product = record['product']
        
        sales_by_rep[rep] += record['total']
        quantity_by_rep[rep] += record['quantity']
        
        sales_by_product[product] += record['total']
        quantity_by_product[product] += record['quantity']
    
    # Create statistics summary
    statistics = {
        'total_records': len(sales_data),
        'total_sales': total_sales,
        'total_quantity': total_quantity,
        'average_sale': average_sale,
        'sales_by_rep': dict(sales_by_rep),
        'quantity_by_rep': dict(quantity_by_rep),
        'sales_by_product': dict(sales_by_product),
        'quantity_by_product': dict(quantity_by_product)
    }
    
    # Display statistics
    print("SALES STATISTICS SUMMARY")
    print("=" * 50)
    print(f"Total Records: {statistics['total_records']}")
    print(f"Total Sales: ${statistics['total_sales']:,.2f}")
    print(f"Total Quantity Sold: {statistics['total_quantity']:,}")
    print(f"Average Sale Amount: ${statistics['average_sale']:.2f}")
    
    print("\nSALES BY REPRESENTATIVE:")
    print("-" * 30)
    for rep, sales in statistics['sales_by_rep'].items():
        quantity = statistics['quantity_by_rep'][rep]
        print(f"{rep}: ${sales:,.2f} ({quantity} items)")
    
    print("\nSALES BY PRODUCT:")
    print("-" * 30)
    for product, sales in statistics['sales_by_product'].items():
        quantity = statistics['quantity_by_product'][product]
        print(f"{product}: ${sales:,.2f} ({quantity} units)")
    
    return statistics

def main():
    filename = "sales_data.csv"
    statistics = calculate_sales_statistics(filename)

if __name__ == "__main__":
    main()
EOF

# 8. Create Summary Report Script (Task 3.1)
echo "Creating create_summary_report.py..."
cat << 'EOF' > create_summary_report.py
#!/usr/bin/env python3
import csv
from collections import defaultdict
from datetime import datetime

def process_sales_and_create_summary(input_filename, output_filename):
    """
    Process sales data and create summary CSV report
    """
    sales_data = []
    
    # Read input CSV file
    try:
        with open(input_filename, 'r', newline='') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            
            for row in csv_reader:
                quantity = int(row['Quantity'])
                price = float(row['Price'])
                total = quantity * price
                
                sale_record = {
                    'date': row['Date'],
                    'product': row['Product'],
                    'category': row['Category'],
                    'quantity': quantity,
                    'price': price,
                    'total': total,
                    'sales_rep': row['Sales_Rep']
                }
                sales_data.append(sale_record)
                
    except FileNotFoundError:
        print(f"Error: Input file '{input_filename}' not found.")
        return False
    except Exception as e:
        print(f"Error reading input file: {e}")
        return False
    
    if not sales_data:
        print("No data to process.")
        return False
    
    # Calculate statistics
    sales_by_rep = defaultdict(lambda: {'total_sales': 0, 'total_quantity': 0, 'num_transactions': 0})
    sales_by_product = defaultdict(lambda: {'total_sales': 0, 'total_quantity': 0, 'num_transactions': 0})
    
    for record in sales_data:
        rep = record['sales_rep']
        product = record['product']
        
        # Update representative statistics
        sales_by_rep[rep]['total_sales'] += record['total']
        sales_by_rep[rep]['total_quantity'] += record['quantity']
        sales_by_rep[rep]['num_transactions'] += 1
        
        # Update product statistics
        sales_by_product[product]['total_sales'] += record['total']
        sales_by_product[product]['total_quantity'] += record['quantity']
        sales_by_product[product]['num_transactions'] += 1
    
    # Write summary to CSV file
    try:
        with open(output_filename, 'w', newline='') as csvfile:
            fieldnames = ['Type', 'Name', 'Total_Sales', 'Total_Quantity', 'Num_Transactions', 'Avg_Sale_Amount']
            csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            # Write header
            csv_writer.writeheader()
            
            # Write sales representative summary
            for rep, stats in sales_by_rep.items():
                avg_sale = stats['total_sales'] / stats['num_transactions'] if stats['num_transactions'] > 0 else 0
                csv_writer.writerow({
                    'Type': 'Sales_Rep',
                    'Name': rep,
                    'Total_Sales': round(stats['total_sales'], 2),
                    'Total_Quantity': stats['total_quantity'],
                    'Num_Transactions': stats['num_transactions'],
                    'Avg_Sale_Amount': round(avg_sale, 2)
                })
            
            # Write product summary
            for product, stats in sales_by_product.items():
                avg_sale = stats['total_sales'] / stats['num_transactions'] if stats['num_transactions'] > 0 else 0
                csv_writer.writerow({
                    'Type': 'Product',
                    'Name': product,
                    'Total_Sales': round(stats['total_sales'], 2),
                    'Total_Quantity': stats['total_quantity'],
                    'Num_Transactions': stats['num_transactions'],
                    'Avg_Sale_Amount': round(avg_sale, 2)
                })
        
        print(f"Summary report successfully written to '{output_filename}'")
        return True
        
    except Exception as e:
        print(f"Error writing summary file: {e}")
        return False

def create_detailed_report(input_filename, detailed_output_filename):
    """
    Create a detailed report with enhanced sales data
    """
    try:
        with open(input_filename, 'r', newline='') as input_file, \
             open(detailed_output_filename, 'w', newline='') as output_file:
            
            csv_reader = csv.DictReader(input_file)
            
            # Define output fieldnames (original + calculated fields)
            output_fieldnames = ['Date', 'Product', 'Category', 'Quantity', 'Price', 
                               'Total_Amount', 'Sales_Rep', 'Month', 'Day_of_Week']
            
            csv_writer = csv.DictWriter(output_file, fieldnames=output_fieldnames)
            csv_writer.writeheader()
            
            for row in csv_reader:
                quantity = int(row['Quantity'])
                price = float(row['Price'])
                total_amount = quantity * price
                
                # Parse date for additional information
                try:
                    date_obj = datetime.strptime(row['Date'], '%Y-%m-%d')
                    month = date_obj.strftime('%B')
                    day_of_week = date_obj.strftime('%A')
                except:
                    month = 'Unknown'
                    day_of_week = 'Unknown'
                
                # Write enhanced record
                csv_writer.writerow({
                    'Date': row['Date'],
                    'Product': row['Product'],
                    'Category': row['Category'],
                    'Quantity': quantity,
                    'Price': price,
                    'Total_Amount': round(total_amount, 2),
                    'Sales_Rep': row['Sales_Rep'],
                    'Month': month,
                    'Day_of_Week': day_of_week
                })
        
        print(f"Detailed report successfully written to '{detailed_output_filename}'")
        return True
        
    except Exception as e:
        print(f"Error creating detailed report: {e}")
        return False

def display_summary_file(filename):
    """
    Display the contents of the summary CSV file
    """
    try:
        print(f"\nContents of '{filename}':")
        print("=" * 80)
        
        with open(filename, 'r', newline='') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            
            # Print header
            print(f"{'Type':<12} {'Name':<15} {'Total Sales':<12} {'Quantity':<10} {'Transactions':<12} {'Avg Sale':<10}")
            print("-" * 80)
            
            for row in csv_reader:
                print(f"{row['Type']:<12} {row['Name']:<15} ${float(row['Total_Sales']):<11.2f} "
                      f"{row['Total_Quantity']:<10} {row['Num_Transactions']:<12} ${float(row['Avg_Sale_Amount']):<9.2f}")
        
        print("-" * 80)
        
    except Exception as e:
        print(f"Error displaying summary file: {e}")

def main():
    input_file = "sales_data.csv"
    summary_file = "sales_summary.csv"
    detailed_file = "detailed_sales_report.csv"
    
    print("Processing sales data and creating reports...")
    print("=" * 50)
    
    # Create summary report
    if process_sales_and_create_summary(input_file, summary_file):
        display_summary_file(summary_file)
    
    # Create detailed report
    if create_detailed_report(input_file, detailed_file):
        print(f"\nBoth summary and detailed reports have been created successfully!")
        print(f"Summary report: {summary_file}")
        print(f"Detailed report: {detailed_file}")

if __name__ == "__main__":
    main()
EOF

# 9. Create Verification Script (Task 3.2)
echo "Creating verify_output.py..."
cat << 'EOF' > verify_output.py
#!/usr/bin/env python3
import csv
import os

def verify_csv_file(filename, description):
    """
    Verify that a CSV file exists and display basic information
    """
    if not os.path.exists(filename):
        print(f"❌ {description} file '{filename}' not found!")
        return False
    
    try:
        with open(filename, 'r', newline='') as csvfile:
            csv_reader = csv.reader(csvfile)
            rows = list(csv_reader)
            
            if len(rows) == 0:
                print(f"❌ {description} file '{filename}' is empty!")
                return False
            
            print(f"✅ {description} file '{filename}' verified:")
            print(f"   - Total rows: {len(rows)}")
            print(f"   - Headers: {', '.join(rows[0]) if rows else 'None'}")
            print(f"   - Data rows: {len(rows) - 1}")
            print()
            
            return True
            
    except Exception as e:
        print(f"❌ Error reading {description} file '{filename}': {e}")
        return False

def main():
    print("FILE VERIFICATION REPORT")
    print("=" * 40)
    
    files_to_check = [
        ("students.txt", "Student text"),
        ("sales_data.csv", "Sales data CSV"),
        ("sales_summary.csv", "Sales summary CSV"),
        ("detailed_sales_report.csv", "Detailed sales report CSV")
    ]
    
    all_verified = True
    for filename, description in files_to_check:
        if not verify_csv_file(filename, description):
            all_verified = False
    
    if all_verified:
        print("🎉 All files verified successfully!")
    else:
        print("⚠️  Some files have issues. Please check the output above.")

if __name__ == "__main__":
    main()
EOF

# 10. Create README for GitHub
echo "Creating README.md..."
cat << 'EOF' > README.md
# Lab 6: File Handling with TXT and CSV

## Objectives
- Open and read text files line by line using Python
- Process CSV files using Python's built-in csv module
- Extract and calculate summary statistics from data
- Write processed data and statistics to new CSV files

## Files Included
- **students.txt**: Sample unstructured text data.
- **read_text_file.py**: Script to read text files.
- **process_text_file.py**: Script to process text and calculate simple stats.
- **sales_data.csv**: Sample structured sales data.
- **read_csv_file.py**: Script to read CSVs using `csv` module.
- **calculate_statistics.py**: Advanced processing and grouping.
- **create_summary_report.py**: Generates new summary CSVs from input data.
- **verify_output.py**: Utility script to verify lab completion.

## How to Run
Run the scripts in the following order:
1. \`python3 read_text_file.py\`
2. \`python3 process_text_file.py\`
3. \`python3 read_csv_file.py\`
4. \`python3 calculate_statistics.py\`
5. \`python3 create_summary_report.py\`
6. \`python3 verify_output.py\`
EOF

echo "Setup complete! All files created in directory: lab6_file_handling"
