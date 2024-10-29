def get_operation():
    print("Select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    
    while True:
        choice = input("Enter your choice (1/2/3/4/5): ")
        if choice in ['1', '2', '3', '4', '5']:
            return choice
        else:
            print("Invalid input. Please choose a valid option.")

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def perform_operation(choice):
    if choice == '5':
        print("Thank you for using the calculator")
        return False
    
    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")

    if choice == '1':
        result = num1 + num2
        operation = "adding"
    elif choice == '2':
        result = num1 - num2
        operation = "subtracting"
    elif choice == '3':
        result = num1 * num2
        operation = "multiplying"
    elif choice == '4':
        if num2 == 0:
            print("Error: Cannot divide by zero.")
            return True
        result = num1 / num2
        operation = "dividing"
    
    print(f"The result of {operation} {num1} and {num2} is {result}.")
    return True

def calculator():
    print("Welcome to the Basic Calculator!")
    
    while True:
        choice = get_operation()
        if not perform_operation(choice):
            break

        another = input("Do you want to perform another calculation? (yes/no): ").lower()
        if another != 'yes':
            print("Thank you for using the calculator. Goodbye!")
            break

calculator()