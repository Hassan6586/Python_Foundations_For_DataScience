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
