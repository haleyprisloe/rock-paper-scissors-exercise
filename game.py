# import random.choice
from random import choice

# intro statement
print("-------------------")
print("Welcome 'Player One' to my Rock-Paper-Scissors game...")
print("-------------------")

# asking for an input
user_choice = input("Please choose either 'rock', 'paper', or 'scissors':")

# create list of options
options = ['rock','paper','scissors']

#validate input
user_choice.lower()
if user_choice not in options:
    print("OOPS, please choose a valid option and try again")
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
print"Thanks for playing")

exit()








