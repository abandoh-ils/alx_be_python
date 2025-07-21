
# Ask the user to input a positive integer for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter for the while loop
row = 0

# Outer loop (while loop) for each row of the pattern
while row < size:
    # Inner loop (for loop) for printing asterisks in each row
    for col in range(size):
        print("*", end="")  # Print '*' without moving to a new line

    print()  # Move to the next line after printing one full row
    row += 1  # Increment the row counter
