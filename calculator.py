num1 = int(input("Enter the number : "))
num2 = 0
result = num1
while True:

    operator = input("Enter the operator (+, -, *, /): and press = to exit: ")
    if (operator == '='):
        break

    num2 = int(input("Enter the number: "))

    # Perform the calculation based on the operator
    if (operator == '+'):
        result = num1 + num2
    # Subtraction
    if (operator == '-'):
        result = num1 - num2
    # Multiplication
    if (operator == '*'):
        result = num1 * num2
    # Division
    if (operator == '/'):
        if num2 == 0:
            # Error handling for division by zero
            print("Error: Division by zero is not allowed.")
            continue
        result = num1 / num2
# Result store here and present here
print("Result: ", result)