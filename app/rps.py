import random

VALID_OPTIONS = ["rock","paper","scissors"]
#ASK USER FOR AN INPUT (RPS) 

user_choice = input("Please choose one of 'rock','paper','scissors'")
print("USER: ", user_choice)

#VALIDATIONS

if user_choice not in VALID_OPTIONS:
    print("Oops, invalid input, please try again")
    exit()
#GENERATE RANDOM COMPUTER CHOICE

computer_choice = random.choice(VALID_OPTIONS)
print("COMPUTER: ", computer_choice)
#DETERMINE THE WINNER

