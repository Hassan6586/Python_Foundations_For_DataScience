import json
import os

def read_json_file(filename):
    """
    Read and parse JSON file with comprehensive error handling
    """
    try:
        print(f"Attempting to read JSON file: {filename}")
        
        with open(filename, 'r') as file:
            data = json.load(file)
            print(f"Successfully parsed JSON data from {filename}")
            return data
    
    except FileNotFoundError:
        print(f"Error: JSON file '{filename}' not found")
        return None
    
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format in '{filename}'")
        print(f"JSON Error details: {e}")
        print(f"Error at line {e.lineno}, column {e.colno}")
        return None
    
    except PermissionError:
        print(f"Error: No permission to read '{filename}'")
        return None
    
    except Exception as e:
        print(f"Unexpected error reading JSON file '{filename}': {type(e).__name__}: {e}")
        return None

def write_json_file(filename, data):
    """
    Write data to JSON file with error handling
    """
    try:
        print(f"Attempting to write JSON data to: {filename}")
        
        with open(filename, 'w') as file:
            json.dump(data, file, indent=2)
            print(f"Successfully wrote JSON data to {filename}")
            return True
    
    except TypeError as e:
        print(f"Error: Data is not JSON serializable: {e}")
        return False
    
    except PermissionError:
        print(f"Error: No permission to write to '{filename}'")
        return False
    
    except Exception as e:
        print(f"Unexpected error writing JSON file '{filename}': {type(e).__name__}: {e}")
        return False

def validate_json_structure(data, required_fields):
    """
    Validate JSON data structure
    """
    try:
        if not isinstance(data, dict):
            raise ValueError("JSON data must be a dictionary")
        
        missing_fields = []
        for field in required_fields:
            if field not in data:
                missing_fields.append(field)
        
        if missing_fields:
            raise KeyError(f"Missing required fields: {missing_fields}")
        
        print("JSON structure validation passed")
        return True
    
    except (ValueError, KeyError) as e:
        print(f"Validation error: {e}")
        return False
    
    except Exception as e:
        print(f"Unexpected validation error: {type(e).__name__}: {e}")
        return False

def create_test_json_files():
    """
    Create test JSON files for demonstration
    """
    # Valid JSON file
    valid_data = {
        "name": "John Doe",
        "age": 30,
        "email": "john.doe@example.com",
        "skills": ["Python", "JavaScript", "SQL"],
        "active": True
    }
    write_json_file("valid_data.json", valid_data)
    
    # Create malformed JSON file manually
    malformed_json = '''
    {
        "name": "Jane Doe",
        "age": 25,
        "email": "jane.doe@example.com"
        "skills": ["Python", "Java"]  // Missing comma before this line
    }
    '''
    
    try:
        with open("malformed_data.json", 'w') as file:
            file.write(malformed_json)
        print("Created malformed JSON file for testing")
    except Exception as e:
        print(f"Error creating malformed JSON file: {e}")

# Test the JSON functions
if __name__ == "__main__":
    print("=== Creating test JSON files ===")
    create_test_json_files()
    
    print("\n=== Testing valid JSON file ===")
    data = read_json_file("valid_data.json")
    if data:
        print(f"Loaded data: {data}")
        
        # Validate structure
        required_fields = ["name", "age", "email"]
        validate_json_structure(data, required_fields)
    
    print("\n=== Testing malformed JSON file ===")
    read_json_file("malformed_data.json")
    
    print("\n=== Testing non-existent JSON file ===")
    read_json_file("nonexistent.json")
