class Calculator:
    def __init__(self):
       pass

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Error! Division by zero."

    def calculator(self):
        """Main calculator logic to get user input and perform operations."""
        print("Welcome to the calculator!")
        print("Choose an operation:")
        print("1: Add")
        print("2: Subtract")
        print("3: Multiply")
        print("4: Divide")

        choice = input("Enter the number of the operation you want to perform (1/2/3/4): ")

        if choice in ['1', '2', '3', '4']:
            try:
                self.num1 = float(input("Enter the first number: "))
                self.num2 = float(input("Enter the second number: "))
            except ValueError:
                print("Invalid input! Please enter numbers only.")
                return

            if choice == '1':
                print(f"{self.num1} + {self.num2} = {self.add()}")
            elif choice == '2':
                print(f"{self.num1} - {self.num2} = {self.subtract()}")
            elif choice == '3':
                print(f"{self.num1} * {self.num2} = {self.multiply()}")
            elif choice == '4':
                result = self.divide()
                if isinstance(result, str):
                    print(result)  # Prints error message
                else:
                    print(f"{self.num1} / {self.num2} = {result}")
        else:
            print("Invalid choice! Please select a valid operation (1/2/3/4).")

# Usage example
if __name__ == "__main__":
    calculator = Calculator()
    calculator.calculator()