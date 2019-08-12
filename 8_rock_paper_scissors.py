from random import randint

# Declare list of choices
choices = ['rock', 'paper', 'scissors']
computer = choices[randint(0, 2)]

while True:
    player = input('You choose :  ').lower()
    if player == "rock" or player == "paper" or player == "scissors":
        print("Computer choose : ", computer)
    if player == computer:
        print("Match tie!")
    elif player == "rock":
        if computer == "scissors":
            print("player win!")
        else:
            print("Computer Win!")
    elif player == "paper":
        if computer == "rock":
            print("Player Win!")
        else:
            print("Computer Win!")
    elif player == "scissors":
        if computer == "paper":
            print("Player Win!")
        else:
            print("Computer Win!")
    else:
        print("Invalid input!")
