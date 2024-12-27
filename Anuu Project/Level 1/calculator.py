def calculator():
    # Get user input for the first number
    num1 = float(input("Enter the first number: "))
    
    # Get user input for the second number
    num2 = float(input("Enter the second number: "))
    
    # Get user input for the operator
    operator = input("Enter an operator (+, -, *, /, %): ")

    # Perform the calculation based on the operator
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error: Division by zero is not allowed."
    elif operator == '%':
        result = num1 % num2
    else:
        return "Error: Invalid operator."

    return f"The result of {num1} {operator} {num2} is: {result}"

# Run the calculator function
print(calculator())