import time

# Part 1: Basic while loop example
print("=== Part 1: Basic While Loop ===")
count = 5

print("Basic countdown:")
while count > 0:
    print(count)
    count = count - 1

print("Done!")
print()

# Part 2: Enhanced countdown timer
print("=== Part 2: Enhanced Countdown Timer ===")

def countdown_timer(seconds):
    """
    Creates a countdown timer that counts down from given seconds
    """
    print(f"Starting countdown from {seconds} seconds...")
    
    while seconds > 0:
        # Display current time in minutes:seconds format
        minutes = seconds // 60
        secs = seconds % 60
        
        if minutes > 0:
            print(f"Time remaining: {minutes:02d}:{secs:02d}")
        else:
            print(f"Time remaining: {secs} seconds")
        
        time.sleep(1)  # Wait for 1 second
        seconds -= 1
    
    print("Time's up! ⏰")

# Get user input for countdown duration
try:
    duration = int(input("\nEnter countdown duration in seconds: "))
    if duration > 0:
        countdown_timer(duration)
    else:
        print("Please enter a positive number.")
except ValueError:
    print("Please enter a valid number.")
