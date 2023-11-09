#SAJJAD ABDIRAHIM GEDOW
#REG: SCT211-0065/2022
#ASSIGNMENT 3 - OOP CALCULATOR

class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            return "Cannot divide by zero."

def main():
    calculator = Calculator()

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    operation = input("Enter the operation (+, -, *, /): ")
    if operation == "+":
        result = calculator.add(num1, num2)
    elif operation == "-":
        result = calculator.subtract(num1, num2)
    elif operation == "*":
        result = calculator.multiply(num1, num2)
    elif operation == "/":
        result = calculator.divide(num1, num2)
    else:
        print("Invalid operation.")
        return

    print("The result is: ", result)

if __name__ == "__main__":
    main()

