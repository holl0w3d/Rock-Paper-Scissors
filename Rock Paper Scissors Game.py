import random

options = ["rock", "paper", "scissors"]

while True:
    player = input("Enter rock, paper, or scissors: ").lower()
    computer = random.choice(options)

    print(f"Computer chose: {computer}")

    if player == computer:
        print("It's a tie!")
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print("You win!")
    else:
        print("You lose!")

    again = input("Play again? (y/n): ").lower()
    if again != "y":
        print("Thanks for playing!")
        break
