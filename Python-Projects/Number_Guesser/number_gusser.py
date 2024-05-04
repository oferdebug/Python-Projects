"""
This script is a simple number guessing game. It generates a random number within a specified range
and prompts the user to guess the number until they guess correctly or choose to exit.
"""
import random

# Get the top of the range from user input
top_of_range = input("Type Of Number: ")

# Check if the input is a valid number
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    # Check if the number is positive
    if top_of_range <= 0:
        print("Please enter a number greater than 0 next time.")
        quit()
else:
    # Notify the user to enter a number next time
    print("Please enter a valid number next time.")
    quit()

# Generate a random number within the specified range
random_number = random.randint(0, top_of_range)
guesses = 0

# Main game loop
while True:
    guesses += 1
    # Get user's guess
    user_guess = input("Guess A Number: ")

    # Check if the user wants to exit
    if user_guess.lower() == 'exit':
        print("Exiting the program...")
        break  # Exit the loop if the user chooses to exit

    # Check if the input is a valid number
    if user_guess.isdigit():
        user_guess = int(user_guess)

        # Check if the user's guess matches the random number
        if user_guess == random_number:
            print("You Got It!")
            break  # Exit the loop if the guess is correct
        elif user_guess > random_number:
            print("Too High")
        else:
            print("Too Low")
    else:
        # Notify the user to enter a valid number or exit
        print("Please enter a valid number or type 'exit' to quit.")

# Print the number of guesses it took to guess the correct number
print("You Got It In", guesses, "Guesses")
