import time

def simple_countdown():
    """Simple countdown timer without complex features"""
    try:
        seconds = int(input("Enter countdown time in seconds: "))
        
        print(f"\nStarting countdown from {seconds} seconds...\n")
        
        while seconds > 0:
            print(f"⏱️  {seconds} seconds remaining")
            time.sleep(1)
            seconds -= 1
        
        print("🔔 Time's up!")
        
    except ValueError:
        print("Please enter a valid number")
    except KeyboardInterrupt:
        print("\n⏹️ Timer stopped by user")

# Run the simple countdown
simple_countdown()
