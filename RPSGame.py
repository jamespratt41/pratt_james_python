from random import randint

#available weapons - this is stored in an array
choices = ["Rock", "Paper", "Scissors"]
player = False
endGame = False

# resets the lives to three when start has not been pressed
start = False
if start == False:
    computerLives = 3
    playerLives = 3


print("Type any key to start game")
start = input()

# checks to see if the player has initiated the game
while start != False:

    # Checks to see if the player has made an input
    while player == False:

        #make the computer pick an item at random
        computer_choice = choices[randint(0,2)]


        #print the text along with the computers choice to the screen
        if endGame == False:
            # prints the amaount of lives each player has and what the computer has chosen.
            print("\nComputer has ", computerLives, " lives.")
            print("Player has ", playerLives, " lives.")
            print("Computer chooses:", computer_choice)
            # prints the player choices and their choice
            print('Choose your weapon')
            player = input("Rock, Paper, or Scissors?\n")
            print("player chooses:", player)

        if endGame == True:
            player = input()

        if(player == computer_choice):
            print("TIE!")

        elif(player == "Rock"):
            if(computer_choice == "Paper"):
                print("Paper covers Rock")
                playerLives = playerLives -1
                # end game check. Also resets game
                if playerLives== 0:
                    print("YOU LOSE! TRY HARDER NEXT TIME! \n Type 'Quit' to leave, or 'Reset' to play again.")
                    endGame = True

            if(computer_choice == "Scissors"):
                print("Rock smashes Scissors")
                computerLives = computerLives -1
                if computerLives== 0:
                    print("YOU WIN! YOU'RE REALLY COOL! \n Type 'Quit' to leave, or 'Reset' to play again.")
                    endGame = True

        elif(player == "Paper"):
            if(computer_choice == "Scissors"):
                print("Scossors cut Paper")
                playerLives = playerLives -1
                # end game check. Also resets game
                if playerLives== 0:
                    print("YOU LOSE! TRY HARDER NEXT TIME! \n Type 'Quit' to leave, or 'Reset' to play again.")
                    endGame = True

            if(computer_choice == "Rock"):
                print("Paper covers Rock")
                computerLives = computerLives -1
                if computerLives== 0:
                    print("YOU WIN! YOU'RE REALLY COOL! \n Type 'Quit' to leave, or 'Reset' to play again.")
                    endGame = True

        elif(player == "Scissors"):
            if(computer_choice == "Rock"):
                print("Rock Smashes Scissors")
                playerLives = playerLives -1
                # end game check. Also resets game
                if playerLives== 0:
                    print("YOU LOSE! TRY HARDER NEXT TIME! \n Type 'Quit' to leave, or 'Reset' to play again.")
                    endGame = True

            if(computer_choice == "Paper"):
                print("Scissors cut Paper")
                computerLives = computerLives -1
                if computerLives== 0:
                    print("YOU WIN! YOU'RE REALLY COOL! \n Type 'Quit' to leave, or 'Reset' to play again.")
                    endGame = True

        # if player types quit, the game will end
        elif player == "Quit":
            exit()

        # if the player types reset, the lives are restored and the enGame variable is reset
        elif player == "Reset":
            computerLives = 3
            playerLives = 3
            endGame = False

        else:
            print("Not a valid input")



    player = False
    computer_choice = choices[randint(0,2)]
