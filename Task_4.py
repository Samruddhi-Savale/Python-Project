# Task 4:
# Rock, Paper, Scissors Game
""" Craete a program that allows the user to play the classic game of rock, paper, scissors
    against the computer"""

import random
options = ["Rock", "Paper", "Scissors"]
user = input("Choose: Rock, Paper, or Scissors: ")
computer = random.choice(options)
print("You chose: ",user)
print("Computer chose: ",computer)
if user == computer:
    print("It's a tie!")
elif user == "Rock" and computer == "Scissors":
    print("You Win!")
elif user == "Paper" and computer == "Rock":
    print("you Win!")
elif user == "Scissors" and computer == "Paper":
    print("You Win!")
else:
    print("Computer Wins!")