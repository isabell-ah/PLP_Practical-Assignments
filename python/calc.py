num1 = float(input("Enter first number: "))
num2 = float (input("Enter second number: "))
operation = input("Enter operation (+, -, *, /):  ")

if operation not in ("+", "-", "*", "/"):
    print(f"Invalid Operation! please choose enter one of +, -, *, /")
else:
    if operation == "+":
        result = num1 +num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == " /" and  num2 != 0:
        result = num1 / num2
    else:
        print("error")
print(f"{num1} {operation} {num2} = {result}")