# main.py

# ------------------------------
# Part 1: For Loop - Favorite Foods
# ------------------------------

# Create a list of at least five favorite foods
favorite_foods = ['Ice Cream', 'Fries', 'Chocolate', 'Menudo', 'Puto', 'Chicken', 'Steak']

# Print a heading
print("Here are my favorite foods:")

# Use a for loop to iterate through the list and print each food
for food in favorite_foods:
    print(f"- {food}")

# Add a blank line to separate outputs
print("\n")

# ------------------------------
# Part 2: While Loop - Countdown
# ------------------------------

# Ask the user to enter a starting number for the countdown
try:
    # Convert user input to an integer
    starting_number = int(input("Enter a positive number to start the countdown: "))

    # Check if the number is greater than zero
    if starting_number <= 0:
        print("Invalid input: Please enter a number greater than zero.")
    else:
        print("Countdown:")
        # Use a while loop to count down from the starting number to 1
        while starting_number > 0:
            print(starting_number)
            starting_number -= 1  # Decrease the number by 1

        # Print message after countdown finishes
        print("Countdown complete!")

# Handle invalid (non-integer) input
except ValueError:
    print("Invalid input: Please enter a positive integer.")
