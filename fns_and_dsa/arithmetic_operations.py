def perform_operation():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

    try:
        if operation == "add":
            result = num1 + num2
        elif operation == "subtract":
            result = num1 - num2
        elif operation == "multiply":
            result = num1 * num2
        elif operation == "divide":
            if num2 == 0:
                print('Error: Division by zero.')
                return  # Exit the function early
            result = num1 / num2
        else:
            print('Error: Invalid operation.')
            return  # Exit the function early

        print(f'The result of {operation} {num1} and {num2} is: {result}')

    except Exception as e:
        print('Error:', e)

# Call the function
perform_operation()
