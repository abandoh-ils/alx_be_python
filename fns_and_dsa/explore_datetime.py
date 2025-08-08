# This script demonstrates basic usage of Python's datetime module
# to display the current date and time, and calculate a future date

from datetime import datetime, timedelta


def display_current_datetime():
    """
    Obtain and print the current date and time in the format YYYY-MM-DD HH:MM:SS.
    """
    # Get the current local date and time
    current_date = datetime.now()
    # Format the datetime object into a human-readable string
    formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted}")


def calculate_future_date(days_to_add):
    """
    Calculate and print the date after adding a given number of days to today.

    Parameters:
    - days_to_add (int): Number of days to add to the current date.
    """
    # Get today's date (without time)
    today = datetime.now().date()
    # Create a timedelta representing the number of days to add
    delta = timedelta(days=days_to_add)
    # Compute the future date
    future_date = today + delta
    # Format and output the new date
    print(f"Future date (+{days_to_add} days): {future_date.strftime('%Y-%m-%d')}")


def main():
    """
    Main function to drive the script:
    1. Display current datetime.
    2. Prompt the user for days to add.
    3. Calculate and display the future date.
    """
    # Part 1: Show current date and time
    display_current_datetime()

    # Part 2: Ask the user for how many days to add
    try:
        user_input = input("Enter the number of days to add to the current date: ").strip()
        days = int(user_input)
    except ValueError:
        # Handle non-integer input gracefully
        print("Invalid input. Please enter an integer number of days.")
        return

    # Calculate and display the future date
    calculate_future_date(days)


# Ensure main() runs when this file is executed directly
if __name__ == "__main__":
    main()
