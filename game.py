# import random.choice
from random import choice

import os

from dotenv import load_dotenv

# setting environment variables

load_dotenv() # invokes / uses the function we got from the third-party package. this one happens to read env vars from the ".env" file. see the package docs for more info

USER_NAME = os.getenv("USER_NAME", default="Player One") # uses the os module to read the specified environment variable and store it in a corresponding python variable


# intro statement
print("-------------------")
print("Welcome to my Rock-Paper-Scissors game...")
print(f"PLAYER: '{USER_NAME}'")
print("-------------------")

# asking for an input
user_choice = input("Please choose either 'rock', 'paper', or 'scissors':")

# create list of options
options = ['rock','paper','scissors']

#validate input
user_choice.lower()
if user_choice not in options:
    print("OOPS, please start again and choose a valid option")
    exit()

# print user input
print(f"You chose: {user_choice}")

# simulating a computer input
computer_choice = choice(options)

# print computer input
print(f"The computer chose: {computer_choice}")


# determining who won
if user_choice == computer_choice:
    print("It's a tie!")
elif user_choice == "paper" and computer_choice == "rock":
    print("You win! Congrats")
elif user_choice == "paper" and computer_choice == "scissors":
    print("Oh! The computer won, that's ok!")
elif user_choice == "rock" and computer_choice == "paper":
    print("Oh! The computer won, that's ok!")
elif user_choice == "rock" and computer_choice == "scissors":
    print("You win! Congrats")
elif user_choice == "scissors" and computer_choice == "paper":
    print("You win! Congrats")
elif user_choice == "scissors" and computer_choice == "rock":
    print("Oh! The computer won, that's ok!")

#farewell message
print("-------------------")
print("Thanks for playing!")
print("-------------------")

exit()








