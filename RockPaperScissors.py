import random
from re import T

states = ["Rock", "Paper", "Scissors"]

def introduction():
    print("Welcome to Andrew's First Python Program: Rock, Paper, Scissors!")
    print("You'll be playing against an AI that'll choose one of the three choices.")
    print()

def get_user_input():
    print("What would you like to play?")
    user_input = input("Rock (R), Paper (P), or Scissors (S)?: ").lower()
    
    while True:
        if user_input[0] == "r":
            return "Rock"
        elif user_input[0] == "s":
            return "Scissors"
        elif user_input[0] == "p":
            return "Paper"
        else:
            print("Please try to choose a valid choice:")
            user_input = input("Rock (R), Paper (P), or Scissors (S)?: ").lower()

def confirm_user_input(user_input):
    print(f"You chose {user_input}")
    confirmation = input(f"To make sure this is the right choice, please type in \"Yes\" if your choice of {user_input} is correct: ").lower()
    tries = 3
    
    for x in range(0, 2):
        if confirmation == "yes":
            return True
        else:
            print("Please try again")
            confirmation = input(f"To make sure this is the right choice, please type in \"Yes\" if your choice of {user_input} is correct: ").lower()
    
def get_computer_choice():
    print(".")
    print(".")
    print(".")
    random_state = random.choice(states)
    print(f"Computer has choosen: {random_state}")
    return random_state

def outcome(user_input, computer_choice):
    wins = {
        states[0]: states[2],
        states[1]: states[0],
        states[2]: states[1]
    }
    
    if user_input == computer_choice:
        print("TIE")
    else:
        if wins.get(user_input) == computer_choice:
            print(f"USER WINS: {user_input} beats {computer_choice}")
        else:
            print(f"USER LOSES: {computer_choice} beats {user_input}")
            
def play_again():
    response = input("Would you like to play again? (Type \"Yes\" or \"No\"): ").lower()
    
    return response == "yes"


introduction()

while True:
    user_input = get_user_input()
    confirmation = confirm_user_input(user_input)
    if confirmation:
        computer_choice = get_computer_choice()
        outcome(user_input, computer_choice)
        if(not play_again()):
            print("Thank you for playing :) Please continue to support my future projects!")
            break
    else:
        print("I am going to assume you do not what to pay the game so I will end the program here. Thank you for making it this far!")
        break


