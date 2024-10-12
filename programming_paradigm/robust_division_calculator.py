# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """Perform division with error handling for division by zero and non-numeric inputs."""
    try:
        # Attempt to convert inputs to float
        num = float(numerator)
        denom = float(denominator)

        # Perform division
        result = num / denom
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
