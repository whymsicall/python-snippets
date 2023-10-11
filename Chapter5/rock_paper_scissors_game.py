# File: rock_paper_scissors_game.py
# Description: Rock Paper Scissors Game
# Assignment Name and Number: #21 of Chapter 5
#
# Name: Landon Svatek
# GitHub: whymsicall
#
# On my honor, Landon Svatek, this programming assignment is my own work
# and I have not provided this code to any other student.

import random

def user_input():
    while True:
        user_choice = input("Choose Rock, Paper, or Scissors: ").strip().lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice")

def rpc_bot():
    rpc_choices = ['rock', 'paper', 'scissors']
    return random.choice(rpc_choices)

def determine_the_winner(user_choice, rpc_choices):
    if user_choice == rpc_choices:
        print("Its a tie!")
    elif user_choice == 'rock' and rpc_choices == 'scissors':
        print("You win!")
    elif user_choice == 'paper' and rpc_choices == 'rock':
        print("You win!")
    elif user_choice == 'scissors' and rpc_choices == 'paper':
        print("You win!")
    else:
        print("You lose!")

def main():
    while True:
        user_choice = user_input()
        rpc_choices = rpc_bot()

        print(f"You chose {user_choice}")
        print(f"The computer chose {rpc_choices}")

        result = determine_the_winner(user_choice, rpc_choices)
        print(result)

if __name__ == '__main__':
    print("Lets play a game of rock paper scissors")
    main()