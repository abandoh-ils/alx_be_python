# Prompting the user to enter the first number
num1 = int(input("Enter the first number: "))

# Prompting the user to enter the second number
num2 = int(input("Enter the second number: "))

# Asking the user to choose the type of operation
opr = input("Choose the operation (+, -, *, /): ")

match opr:
    case '+':
        result = num1 + num2
        print("The result is {}.".format(result))

    case '-':
        result = num1 - num2
        print("The result is {}.".format(result))

    case '*':
        result = num1 * num2
        print("The result is {}.".format(result))

    case '/':
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1 + num2
            print("The result is {}.".format(result))

    case _:
        # Handle any other unexpected operator
        print("Invalid operation selected. Please choose from +, -, *, /.")