number1 = float(input("Enter the first number for the operation:"))

number2 = float(input("Enter the second number for the operation:"))

operation = input("Enter the operation symbol for the operation:")


if operation == "*":
    print(number1 * number2)

elif operation == "+":
    print(number1 + number2)

elif operation == "-":
    if number1 > number2:
        print(number1 - number2)
    else:
        print(number2 - number1)

elif operation == "/" or operation == ":":
    if number2 != 0:
        print(number1 / number2)
    else:
        print("Cannot divide by zero!")

elif operation == "^":
    print(number1**number2)

else:
    print("Invalid operation symbol entered.")
