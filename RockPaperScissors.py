import random

states = ["Rock", "Paper", "Scissors"]

def introduction():
    print("Welcome to Andrew's First Python Program: Rock, Paper, Scissors!")
    print("You'll be playing against an AI that'll choose one of the three choices.")
    print()

def get_user_input():
    print("What would you like to play?")
    user_input = input("Rock (R), Paper (S), or Scissors (S)?: ").lower()
    
    while True:
        if user_input[0] == "r":
            return "Rock"
        elif user_input[0] == "s":
            return "Scissors"
        elif user_input[0] == "p":
            return "Paper"
        else:
            print("Please try to choose a valid choice:")
            user_input = input("Rock (R), Paper (S), or Scissors (S)?: ").lower()


    return user_input

def confirm_user_input(user_input):
    print(f"You chose {user_input}")
    confirmation = input(f"To make sure this is the right choice, please type in \"Yes\" if your choice of {user_input} is correct ")
    tries = 3
    
    for x in range(0, 2):
        if confirmation == "yes":
            return True
        else:
            print("Please try again")
            confirmation = input(f"To make sure this is the right choice, please type in \"Yes\" if your choice of {user_input} is correct ")
    else:
        print("I am going to assume you do not what to pay the game so I will end the program here. Thank you for making it this far!")
        return False



introduction()
user_input = get_user_input()
confirmation = confirm_user_input(user_input)
    



