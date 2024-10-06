FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9  # Conversion factor for F to C
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5  # Conversion factor for C to F


def convert_to_celsius(fahrenheit):
    """Converts temperature from Fahrenheit to Celsius.

    Args:
        fahrenheit (float): Temperature in Fahrenheit.

    Returns:
        float: Temperature in Celsius.
    """

    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius


def convert_to_fahrenheit(celsius):
    """Converts temperature from Celsius to Fahrenheit.

    Args:
        celsius (float): Temperature in Celsius.

    Returns:
        float: Temperature in Fahrenheit.
    """

    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit


def main():
    while True:
        try:
            # Get temperature and unit from user
            temperature = float(input("Enter the temperature to convert: "))
            unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

            if unit not in ("C", "F"):
                raise ValueError("Invalid unit. Please enter 'C' or 'F'.")

            # Convert temperature based on unit
            if unit == "C":
                converted_temperature = convert_to_fahrenheit(temperature)
                converted_unit = "F"
            else:
                converted_temperature = convert_to_celsius(temperature)
                converted_unit = "C"

            # Display the converted temperature
            print(f"{temperature:.1f}°{unit} is {converted_temperature:.1f}°{converted_unit}")
            break

        except ValueError as e:
            print(f"Error: {e}")
            print("Please enter a valid numeric value and unit (C/F).")


if __name__ == "__main__":
    main()