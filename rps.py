import random

print("Let's play a game of Jan Ken!")

user_action = input("Enter rock, paper, or scissors: ").lower()

possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)

print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

match user_action:
    case _ if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")

    case "rock":
        match computer_action:
            case "scissors":
                print("Rock smashes scissors! You win!")
            case "paper":
                print("Paper covers rock! You lose.")

    case "paper":
        match computer_action:
            case "rock":
                print("Paper covers rock! You win!")
            case "scissors":
                print("Scissors cuts paper! You lose.")

    case "scissors":
        match computer_action:
            case "paper":
                print("Scissors cuts paper! You win!")
            case "rock":
                print("Rock smashes scissors! You lose.")

    case _:
        print("Invalid input! Please enter rock, paper, or scissors.")
