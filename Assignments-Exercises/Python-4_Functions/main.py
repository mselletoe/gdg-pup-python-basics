# main.py

# ------------------------------
# Function to create a greeting message
# ------------------------------
def create_greeting(name):
    """
    Create a personalized greeting message.

    Parameters:
        name (str): The name to include in the greeting.

    Returns:
        str: The greeting message.
    """
    return (f"Hello {name}, welcome to the GDG Web Development Team! You're doing great, "
            f"and I truly believe that someday you'll be an amazing developer. Life may feel "
            f"challenging right now, and programming can be overwhelming at times, but remember, "
            f"all your hard work will pay off in the end. Keep pushing forward, you're on the right path!")

# ------------------------------
# Main program
# ------------------------------
try:
    # Ask the user to enter their name
    name = input("Enter your name: ").strip()

    # Check if input is not empty and only contains alphabetic characters and spaces
    if not name or not all(part.isalpha() for part in name.split()):
        raise ValueError

    # Create and display the greeting message
    greeting = create_greeting(name)
    print(f"The greeting message is: {greeting}")

except ValueError:
    print("Invalid input: Please enter a valid name.")