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

# DETERMINE THE WINNER

# quick alias to facilitate some copy and pasting
# we will soon move this into a function anyway
u = user_choice
c = computer_choice

if u == "rock" and c == "rock":
    print("TIE GAME")
elif u == "rock" and c == "paper":
    print("COMPUTER WINS")
elif u == "rock" and c == "scissors":
    print("USER WINS")
elif u == "paper" and c == "rock":
    print("COMPUTER WINS") # OOPS
elif u == "paper" and c == "paper":
    print("TIE GAME")
elif u == "paper" and c == "scissors":
    print("USER WINS") # OOPS
elif u == "scissors" and c == "rock":
    print("COMPUTER WINS")
elif u == "scissors" and c == "paper":
    print("USER WINS")
elif u == "scissors" and c == "scissors":
    print("TIE GAME")
    