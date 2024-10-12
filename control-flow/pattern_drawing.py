# pattern_drawing.py

def draw_pattern():
    # Prompt user for pattern size
    size = int(input("Enter the size of the pattern: "))
    
    # Ensure the input is a positive integer
    if size <= 0:
        print("Please enter a positive integer.")
        return
    
    # Use a while loop to iterate through each row
    row = 0
    while row < size:
        # Use a for loop to print asterisks side by side
        for col in range(size):
            print("*", end="")
        # Move to the next line after completing a row
        print()
        row += 1

# Call the function to execute the program
if __name__ == "__main__":
    draw_pattern()
