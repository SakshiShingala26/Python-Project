"""NUMBER GUESSING GAME
1.Generates a random integer between the lower and upper bounds (inclusive).
2.Asks the user to guess the number.
3.Use a loop to allow the user multiple attempts.
4.Provide feedback after each guess.
5.End the game when the user guesses correctly or runs out of attempts.
"""

import random 

def number_guessing_game():
    print("*"*70)
    print(" "*15,"WELCOME TO THE NUMBER GUESSING GAME")
    print("*"*70)
    
    
    # set the value for upper limit and lower limit for guess the number
    lower_bound=1
    upper_bound=100
    
    # generate a random number
    number_to_guess=random.randint(lower_bound,upper_bound)
    
    # set the total attempt to guess the number by user
    attempts=5
    
    print(" ")
    print(f"You have selected a number between {lower_bound} and {upper_bound}.")
    print(f"You have {attempts} attempts to guess it.")
    print(" ")
    print("*"*50)
    
    # check the number using for else statements
    for attempt in range(1, attempts + 1):
        guess = int(input(f"Attempt {attempt}: Enter your guess: "))
        
        if guess < number_to_guess:
            print("Too low!")
            print(" ")
        elif guess > number_to_guess:
            print("Too high!")
            print(" ")
        else:
            print(f"Congratulations! You've guessed the number {number_to_guess} in {attempt} attempts.")
            print(" ")
            break
    else:
        print(f"Sorry, you've used all your attempts. The number was {number_to_guess}.")
        print(" ")
    
    print("*"*70)
    print("Game Over. Thanks for playing!")
    print("*"*70)
    
    
# functionn calling
number_guessing_game()