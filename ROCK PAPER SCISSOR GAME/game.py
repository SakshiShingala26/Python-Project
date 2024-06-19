"""
WORKFLOW OF PROJECT:
1- Input from user(Rock, paper, scissor)
2- Computer choice (Computer will choose randomly not conditionally)
3- Result print

Cases:
A- Rock
Rock - Rock = tie
Rock - Paper = Paper win
Rock - scissor = Rock win

B- Paper
Paper - Paper = tie
Paper - Rock = Paper win
Paper - Scissor = Scissor win

C- Scissor
Scissor - Scissor = tie
Scissor - Rock = Rock win
Scissor - Paper = Scissor win

"""
import random
item_list=["Rock","Paper","Scissor"]

print("*"*80)
print(" "*15,"WELCOME TO THE ROCK , PAPER , SCISSOR GAME")
print("*"*80)
# enter by user
user_choice=input("Enter any one to play :: (Rock,Paper,Scissor) :: \n")
# choose bye compuer randomly
computer_choice=random.choice(item_list)

print(" ")
print(f"User choice :: {user_choice}\nComputer choice :: {computer_choice}")
print(" ")

if(user_choice == computer_choice):
    print("Both choices are same := Match Tie")

# user choice is Rock
elif(user_choice == "Rock"):
    # computer choice is paper
    if (computer_choice == "Paper"):
        print("Paper covers the Rock := Computer Win")
    # computer choice is scissor
    else:
        print("Rock crushes the Scissor := You Win")
        
# user choice is Paper
elif(user_choice == "Paper"):
    # computer choice is rock
    if (computer_choice == "Rock"):
        print("Paper covers the Rock := You Win")
    # computer choice is scissor
    else:
        print("Scissor cuts the Paper := Computer Win")
        
# user choice is Scissor
elif(user_choice == "Scissor"):
    # computer choice is rock
    if (computer_choice == "Rock"):
        print("Rock crushes the Scissor := Computer Win")
    # computer choice is paper
    else:
        print("Scissor cuts the Paper := You Win")

print(" ")
print("*"*80)
print(" "*15,"THANK YOU FOR PLAING GAME!! GAME OVER")
print("*"*80)
print(" ")