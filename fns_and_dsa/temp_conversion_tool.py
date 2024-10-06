# temp_conversion_tool.py  

# Define Global Conversion Factors  
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FREEZING_POINT_FAHRENHEIT = 32


def convert_to_celsius(fahrenheit):
    """Convert a temperature from Fahrenheit to Celsius."""
    celsius = (fahrenheit - FREEZING_POINT_FAHRENHEIT) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius


def convert_to_fahrenheit(celsius):
    """Convert a temperature from Celsius to Fahrenheit."""
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FREEZING_POINT_FAHRENHEIT
    return fahrenheit


def main():
    """Main function to handle user interaction for temperature conversion."""
    try:
        temperature = input("Enter the temperature to convert: ")
        temperature = float(temperature)  # Convert input to float to validate numeric value

        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == 'F':
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp:.2f}°C")

        elif unit == 'C':
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp:.2f}°F")

        else:
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError as e:
        print(f"Invalid input: {e}. Please enter a numeric temperature.")

    # Run the main function when the script is executed


if __name__ == "__main__":
    main()