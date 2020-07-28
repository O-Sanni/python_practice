# Write a programme where the computer randomly generates a number between 0 and 20. 
# The user needs to guess what the number is. If the user guesses wrong, tell them their guess is either too high, or too low. 
# This will get you started with the random library if you haven't already used it.

import random

user_guess=0
generated_num=0

def game():
    global generated_num
    generated_num=random.randrange(0,21)
    global user_guess
    user_guess=int(input("Please enter number from 0 to 20, or enter 21 to exit "))
    while (True):
        if user_guess==generated_num:
            break
        if user_guess==21:
            break
        elif user_guess not in range(0,21):
            user_guess=int(input("You enter wrong value, please try again or enter 21 to exit "))
        elif user_guess<generated_num:
            user_guess=int(input("Your number is less then guessing number, please try again or enter 21 to exit ")) 
        elif user_guess>generated_num:
            user_guess=int(input("Your number is more then guessing number, please try again or enter 21 to exit "))  

repeat_game=True

while input:
    game()
    print(user_guess)
    print(generated_num)   
    if user_guess==generated_num:
        gameint=input(f'Congratulations you win {user_guess} is correct, if you want to repeat the game please enter y otherwise press any button ')
        if gameint=="y":
            pass
        else:
            break
    elif user_guess==21:
        gameint= input("You press exit, if you want to start over please press y otherwise press any button ")
        if gameint=="y":
           pass
        else:
            break


    

    
    
    