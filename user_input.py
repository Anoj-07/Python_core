# Rock paper scissors game
import sys 
import random

print('')

player_choice = input("Enter ... \n1 for Rock, \n2 for Paper, \n3 for Scissors:\n\n")
player = int(player_choice)

if player < 1 or player > 3:
    sys.exit('You must enter 1, 2, or 3.')

computer_choice = random.choice("123")
computer = int(computer_choice)

print("")
print("You chose: " + player_choice)
print("Computer chose: " + computer_choice)

print("--------------------------------")

if player ==1 and computer == 3:
    print("You win!")
elif player == 2 and computer == 1:
    print("You win!")
elif player == 3 and computer == 2:
    print("You wins!")
elif player == computer:
    print("Tie game!")
else:
    print("Computer wins!")