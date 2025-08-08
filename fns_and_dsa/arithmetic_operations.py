# defining the perform operatiosn function
def perform_operation(num1, num2, operation):
    """
    Perform a basic arithmetic operation on two numbers.

    Parameters:
    - num1 (float): The first operand.
    - num2 (float): The second operand.
    - operation (str): A string indicating the operation to perform.
                       Valid values are 'add', 'subtract', 'multiply', 'divide'.

    Returns:
    - float or str: The result of the arithmetic operation, or an error message
                    if the operation is invalid or if there's division by zero.
    """

    # normalize the operation string to lower case and remove extra space
    op = operation.strip().lower()

    # Addition
    if op == 'add':
        # Simply return the sum of num1 and num2
        return num1 + num2

    # Subtraction
    elif op == 'subtract':
        # Return the difference (num1 minus num2)
        return num1 - num2

    # Multiplication
    elif op == 'multiply':
        # Return the product of num1 and num2
        return num1 * num2

    # Division
    elif op == 'divide':
        # Before dividing, check for division by zero
        if num2 == 0:
            # Return a clear error message that main.py can display
            return "Error: Division by zero is not allowed."
        # Perform the division if safe
        return num1 / num2

    # If we reach here, the operation string wasn't one of the expected ones
    else:
        # Return an error message for an unrecognized operation
        return f"Error: Unsupported operation '{operation}'. Valid operations are add, subtract, multiply, divide."
       