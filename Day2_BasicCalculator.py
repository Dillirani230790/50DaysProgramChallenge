def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_operator():
    valid_operators = ['+', '-', '*', '/']
    while True:
        op = input("Enter operator (+, -, *, /): ").strip()
        if op in valid_operators:
            return op
        print("Invalid operator. Please choose from +, -, *, /.")

def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2

def main():
    print("Welcome to Python Calculator")
    while True:
        num1 = get_number("Enter the first number: ")
        operator = get_operator()
        num2 = get_number("Enter the second number: ")
        
        result = calculate(num1, num2, operator)
        print(f"Result: {result}")

        choice = input("Do you want to perform another calculation? (y/n): ").strip().lower()
        if choice != 'y':
            print("Thank you for using the calculator!")
            break

if __name__ == "__main__":
    main()
