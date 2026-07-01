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

    if (operator == '-'):
        result = num1 - num2

    if (operator == '*'):
        result = num1 * num2

    if (operator == '/'):
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            continue
        result = num1 / num2

print("Result: ", result)