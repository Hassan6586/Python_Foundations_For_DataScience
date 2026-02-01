def read_file_basic(filename):
    """
    Basic file reading function without exception handling
    """
    file = open(filename, 'r')
    content = file.read()
    file.close()
    return content

def read_file_with_exceptions(filename):
    """
    File reading function with proper exception handling
    """
    file = None
    try:
        print(f"Attempting to open file: {filename}")
        file = open(filename, 'r')
        content = file.read()
        print(f"Successfully read {len(content)} characters from {filename}")
        return content
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None
    
    except PermissionError:
        print(f"Error: Permission denied to read file '{filename}'.")
        return None
    
    except IOError as e:
        print(f"Error: An I/O error occurred while reading '{filename}': {e}")
        return None
    
    finally:
        # This block always executes, ensuring proper cleanup
        if file and not file.closed:
            file.close()
            print(f"File '{filename}' has been properly closed.")

# Test the functions
if __name__ == "__main__":
    # Test with existing file
    print("=== Testing with existing file ===")
    content = read_file_with_exceptions("file_handler.py")
    
    # Test with non-existing file
    print("\n=== Testing with non-existing file ===")
    content = read_file_with_exceptions("nonexistent.txt")
