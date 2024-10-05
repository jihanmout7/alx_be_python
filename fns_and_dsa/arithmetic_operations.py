def perform_operation(num1,num2,operation):
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()
    try:
        if num1 == 0:
            print('Error divsion by zero')
    except :
        print('Error')

perform_operation()


