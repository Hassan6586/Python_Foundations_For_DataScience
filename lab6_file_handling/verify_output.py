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
