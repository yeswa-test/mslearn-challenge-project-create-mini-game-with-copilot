import random

def get_player_choice():
    """
    Prompts the player to enter their choice of rock, paper, or scissors.
    Validates the user's input and converts it to lowercase.
    """
    while True:
        player_choice = input("Choose rock, paper, or scissors: ").lower()
        if player_choice in ["rock", "paper", "scissors"]:
            return player_choice
        else:
            print("Invalid choice. Please try again.")

def get_computer_choice():
    """
    Generates a random choice for the computer (rock, paper, or scissors).
    """
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(player_choice, computer_choice):
    """
    Determines the winner of the round based on the player's and computer's choices.
    Returns the result as a string ("win", "lose", or "tie").
    """
    if player_choice == computer_choice:
        return "tie"
    elif (
        (player_choice == "rock" and computer_choice == "scissors") or
        (player_choice == "paper" and computer_choice == "rock") or
        (player_choice == "scissors" and computer_choice == "paper")
    ):
        return "win"
    else:
        return "lose"

def play_game():
    """
    Runs the Rock-Paper-Scissors game loop.
    """
    player_score = 0
    computer_score = 0

    while True:
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        result = determine_winner(player_choice, computer_choice)

        print(f"You chose {player_choice}, the computer chose {computer_choice}.")
        if result == "win":
            print("You win!")
            player_score += 1
        elif result == "lose":
            print("You lose.")
            computer_score += 1
        else:
            print("It's a tie!")

        print(f"Your score: {player_score}, Computer score: {computer_score}")

        play_again = input("Do you want to play again? (y/n) ").lower()
        if play_again != "y":
            break

    print("Thanks for playing!")

play_game()