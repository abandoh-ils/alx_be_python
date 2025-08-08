FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9       # Multiplier to convert a Fahrenheit delta to Celsius
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5       # Multiplier to convert a Celsius delta to Fahrenheit

def convert_to_celsius(fahrenheit):
    """
    Convert a temperature from Fahrenheit to Celsius.

    Uses the global FAHRENHEIT_TO_CELSIUS_FACTOR for the conversion.
    Formula: (°F − 32) × (5/9)

    Parameters:
        fahrenheit (float): Temperature in degrees Fahrenheit.

    Returns:
        float: Temperature converted to degrees Celsius.
    """
    # Subtract the 32°F offset, then apply the global multiplier
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Convert a temperature from Celsius to Fahrenheit.

    Uses the global CELSIUS_TO_FAHRENHEIT_FACTOR for the conversion.
    Formula: (°C × (9/5)) + 32

    Parameters:
        celsius (float): Temperature in degrees Celsius.

    Returns:
        float: Temperature converted to degrees Fahrenheit.
    """
    # Multiply by the global factor, then add the 32°F offset
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    """
    Main loop of the temperature conversion tool.

    - Prompts the user to enter a temperature value (or 'q' to quit).
    - Prompts the user to specify the unit (C or F).
    - Performs the appropriate conversion and displays the result.
    - Handles invalid inputs gracefully by displaying error messages.
    """
    print("Welcome to the Temperature Conversion Tool!")
    print("You can convert between Celsius and Fahrenheit.")
    print("Type 'q' at any prompt to exit.\n")

    while True:
        # 1. Get the temperature value from the user
        temp_input = input("Enter the temperature to convert: (e.g., 100) ").strip()
        if temp_input.lower() == 'q':
            print("Goodbye!")
            break

        # Validate that the temperature is a number
        try:
            temp_value = float(temp_input)
        except ValueError:
            # If conversion fails, inform the user and restart the loop
            print("Invalid temperature. Please enter a numeric value.\n")
            continue

        # 2. Get the unit of the temperature
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        if unit.lower() == 'q':
            print("Goodbye!")
            break

        # 3. Perform the conversion based on the unit
        if unit == 'F':
            # Convert Fahrenheit to Celsius
            converted = convert_to_celsius(temp_value)
            print(f"\n{temp_value}°F is {converted:.2f}°C\n")

        elif unit == 'C':
            # Convert Celsius to Fahrenheit
            converted = convert_to_fahrenheit(temp_value)
            print(f"\n{temp_value}°C is {converted:.2f}°F\n")

        else:
            # Handle invalid unit entry
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.\n")
            continue

if __name__ == "__main__":
    main()