import random

VALID_OPTIONS = ["rock","paper","scissors"]

if__name__ == "__main__":
    #only run the code below
    #if we are running this script from teh command line
    #but not if we're trying to just import some stuff from this file 

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

    result = determine_winner(user_choice, computer_choice)
    print(result)

def determine_winner(u, c):
    if u == "rock" and c == "rock":
        return "TIE GAME"
    elif u == "rock" and c == "paper":
        return "COMPUTER WINS"
    elif u == "rock" and c == "scissors":
        return "USER WINS"
    elif u == "paper" and c == "rock":
        return "USER WINS"
    elif u == "paper" and c == "paper":
        return "TIE GAME"
    elif u == "paper" and c == "scissors":
        return "COMPUTER WINS" # OOPS
    elif u == "scissors" and c == "rock":
        return "COMPUTER WINS"
    elif u == "scissors" and c == "paper":
        return "USER WINS"
    elif u == "scissors" and c == "scissors":
        return "TIE GAME"

