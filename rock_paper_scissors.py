# Rock, Paper, Scissors Game
# Make a rock-paper-scissors game where it is the player vs the computer. 
# The computer’s answer will be randomly generated, while the program will ask the user for their input. 
# This project will better your understanding of while loops and if statements.

import random


def game():
    while input:
        list_choice=["rock","paper","scissors"]
        compChoice=list_choice[random.randrange(0,3)]
        choice=int(input("Please press 1-rock, 2-paper, 3-scissors, for exit press any other key "))
        if choice in range(1,4):
            userChoice=list_choice[choice-1]
            print(userChoice)
            if userChoice=="rock":
                if userChoice=="rock" and compChoice=="rock":
                    print(f'You both choose {userChoice}, no winner')
                elif userChoice=="rock" and compChoice=="scissors":
                    print(f'You choose {userChoice}, computer choose {compChoice}, you win')
                elif userChoice=="rock" and compChoice=="paper":
                    print(f'You choose {userChoice}, computer choose {compChoice}, computer win')
            elif userChoice=="paper":
                if userChoice=="paper" and compChoice=="paper":
                    print(f'You both choose {userChoice}, no winner')
                elif userChoice=="paper" and compChoice=="rock":
                    print(f'You choose {userChoice}, computer choose {compChoice}, you win')
                elif userChoice=="paper" and compChoice=="scissors":
                    print(f'You choose {userChoice}, computer choose {compChoice}, computer win')
            elif userChoice=="scissors":
                if userChoice=="scissors" and compChoice=="scissors":
                    print(f'You both choose {userChoice}, no winner')
                elif userChoice=="scissors" and compChoice=="paper ":
                    print(f'You choose {userChoice}, computer choose {compChoice}, you win')
                elif userChoice=="scissors" and compChoice=="rock":
                    print(f'You choose {userChoice}, computer choose {compChoice}, computer win')
        else:
            break
        

game()

