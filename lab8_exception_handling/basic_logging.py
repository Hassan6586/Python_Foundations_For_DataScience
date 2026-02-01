import logging
import json
import os
from datetime import datetime

# Configure basic logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('application.log'),
        logging.StreamHandler()  # Also output to console
    ]
)

# Create logger
logger = logging.getLogger(__name__)

def process_file_with_logging(filename):
    """
    Process a file with comprehensive logging
    """
    logger.info(f"Starting file processing for: {filename}")
    
    try:
        # Check if file exists
        if not os.path.exists(filename):
            logger.error(f"File not found: {filename}")
            raise FileNotFoundError(f"File '{filename}' does not exist")
        
        logger.debug(f"File exists, attempting to read: {filename}")
        
        # Read file
        with open(filename, 'r') as file:
            content = file.read()
        
        logger.info(f"Successfully read {len(content)} characters from {filename}")
        
        # Try to parse as JSON
        try:
            data = json.loads(content)
            logger.info(f"Successfully parsed JSON data from {filename}")
            logger.debug(f"JSON data keys: {list(data.keys()) if isinstance(data, dict) else 'Not a dictionary'}")
            return data
        
        except json.JSONDecodeError as e:
            logger.warning(f"File {filename} is not valid JSON, treating as plain text")
            logger.debug(f"JSON parse error: {e}")
            return content
    
    except FileNotFoundError as e:
        logger.error(f"File not found error: {e}")
        raise
    
    except PermissionError as e:
        logger.error(f"Permission denied reading {filename}: {e}")
        raise
    
    except Exception as e:
        logger.critical(f"Unexpected error processing {filename}: {type(e).__name__}: {e}")
        raise
    
    finally:
        logger.info(f"Finished processing attempt for: {filename}")

def create_sample_files():
    """
    Create sample files for logging demonstration
    """
    logger.info("Creating sample files for demonstration")
    
    # Create a JSON file
    sample_data = {
        "timestamp": datetime.now().isoformat(),
        "message": "This is a sample JSON file",
        "data": [1, 2, 3, 4, 5]
    }
    
    try:
        with open("sample.json", 'w') as f:
            json.dump(sample_data, f, indent=2)
        logger.info("Created sample.json successfully")
    except Exception as e:
        logger.error(f"Failed to create sample.json: {e}")
    
    # Create a text file
    try:
        with open("sample.txt", 'w') as f:
            f.write("This is a sample text file\nWith multiple lines\nFor testing purposes")
        logger.info("Created sample.txt successfully")
    except Exception as e:
        logger.error(f"Failed to create sample.txt: {e}")

# Test logging functionality
if __name__ == "__main__":
    logger.info("=== Starting logging demonstration ===")
    
    # Create sample files
    create_sample_files()
    
    # Test with different file types
    test_files = ["sample.json", "sample.txt", "nonexistent.txt"]
    
    for filename in test_files:
        logger.info(f"--- Processing {filename} ---")
        try:
            result = process_file_with_logging(filename)
            logger.info(f"Processing completed for {filename}")
        except Exception as e:
            logger.error(f"Processing failed for {filename}: {e}")
    
    logger.info("=== Logging demonstration completed ===")
    print("\nCheck 'application.log' file for detailed logs!")
