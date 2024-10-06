# Temperature Conversion Tool

# 1. Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_OFFSET = 32  # This is used for conversions

# 2. Implement conversion functions
def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - FAHRENHEIT_OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FAHRENHEIT_OFFSET

# 3. User interaction
def main():
    while True:  # Loop for continuous interaction
        try:
            # User input for temperature
            temp_input = float(input("Enter the temperature to convert: "))
            unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

            if unit == 'C':
                # Convert from Celsius to Fahrenheit
                converted_temp = convert_to_fahrenheit(temp_input)
                print(f"{temp_input}°C is {converted_temp:.2f}°F")
            elif unit == 'F':
                # Convert from Fahrenheit to Celsius
                converted_temp = convert_to_celsius(temp_input)
                print(f"{temp_input}°F is {converted_temp:.2f}°C")
            else:
                print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

        except ValueError:
            print("Invalid temperature. Please enter a numeric value.")

        # Prompt for another conversion
        another = input("Would you like to convert another temperature? (yes/no): ").strip().lower()
        if another != 'yes':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
