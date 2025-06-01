# Prompt the user for the pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# Use a while loop to go through each row
while row < size:
    # Use a for loop to print stars in the current row
    for col in range(size):
        print("*", end="")  # Print on the same line
    print()  # Move to the next line after one row is printed
    row += 1  # Go to the next row
