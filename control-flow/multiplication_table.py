# Prompt the user to enter a number for the multiplication table
number = int(input("Enter a number to see its multiplication table: "))

# Use a for loop to iterate from 1 to 10
for i in range(1, 11):
    # Calculate the product of the entered number and the current loop value
    product = number * i
    
    # Print the result in the format: "X * Y = Z"
    print(f"{number} * {i} = {product}")