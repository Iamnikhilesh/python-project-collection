# CALCULATOR
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

def calculator():
    print("Simple Calculator")
    print("Operations:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    # Input from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation_choice = input("Choose operation (1/2/3/4): ")

    # Perform the calculation based on the user's choice
    if operation_choice == '1':
        result = add(num1, num2)
    elif operation_choice == '2':
        result = subtract(num1, num2)
    elif operation_choice == '3':
        result = multiply(num1, num2)
    elif operation_choice == '4':
        result = divide(num1, num2)
    else:
        result = "Error: Invalid operation"

    # Display the result
    print("Result: {}".format(result))

if __name__ == "__main__":
    calculator()
