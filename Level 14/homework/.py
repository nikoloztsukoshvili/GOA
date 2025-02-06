print("Calculator")
print("Enter two numbers and an operator (+, -, , /)")


num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -,*, /): ")
num2 = float(input("Enter second number: "))


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
        print("Error: Division by zero is not allowed.")
        result = None
else:
    print("Invalid operator. Please use +, -, *, or /.")
    result = None


if result is not None:
    print("The result of " + str(num1) + " " + operator + " " + str(num2) + " is: " + str(result))