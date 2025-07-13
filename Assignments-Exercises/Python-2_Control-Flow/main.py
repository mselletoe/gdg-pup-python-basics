# Loops – For and While Assignment

# -----------------------------------------
# Part 1: For Loop - Printing a list of favorite foods
# -----------------------------------------

# Create a list of favorite foods
favorite_foods = ['Ice Cream', 'Fries', 'Chocolate', 'Menudo', 'Puto', 'Chicken', 'Steak']

# Display a message
print("Here are my favorite foods:")

# Use a for loop to iterate and print each food
for food in favorite_foods:
    print(f"- {food}")  # Each food with a bullet point

# Add a blank line to separate parts
print("\n")

# -----------------------------------------
# Part 2: While Loop - Countdown from a number
# -----------------------------------------

try:
    # Ask user for a starting number
    starting_number = int(input("Enter a positive number to start the countdown: "))

    # Check if the number is positive
    if starting_number <= 0:
        print("Invalid input: Please enter a number greater than zero.")
    else:
        print("Countdown:")
        # Use a while loop to count down to 1
        while starting_number > 0:
            print(starting_number)
            starting_number -= 1
        print("Countdown complete!")  # Final message

# Handle non-integer input
except ValueError:
    print("Invalid input: Please enter a positive integer.")