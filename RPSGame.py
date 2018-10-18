from random import randint

#available weapons - this is stored in an array
choices = ["Rock", "Paper", "Scissors"]

#make the computer pick an item at random

computer_choice = choices[randint(0,2)]

#print the text along with the computers choice to the screen
print("Computer chooses: ", computer_choice)
