import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input(
        "Please Type Rock/Paper/Scissors or Q to Quit: ").lower()

    if user_input not in options and user_input != "q":
        print(
            "Invalid input. Please type Rock, Paper, Scissors, or Q to quit.")
        continue

    if user_input == "q":
        break

    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print("Computer Picked", computer_pick + ".")

    if (user_input == "rock" and computer_pick == "scissors") or \
       (user_input == "paper" and computer_pick == "rock") or \
       (user_input == "scissors" and computer_pick == "paper"):
        print("You Won!")
        user_wins += 1

    elif (user_input == "rock" and computer_pick == "paper") or \
         (user_input == "paper" and computer_pick == "scissors") or \
         (user_input == "scissors" and computer_pick == "rock"):
        print("You Lost!")
        computer_wins += 1

    else:
        print("It's a tie!")

print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Goodbye!")
