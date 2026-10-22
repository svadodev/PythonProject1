import random

inMenu = True
inGame = False

while inMenu:
    detonatorGaming = input("Do you want to play the guessing game? (type 'yes' or 'no') \n")
    if detonatorGaming == "yes":
        choice = input("Which mode do you want to play? 1-10, 1-50, or 1-100? (type 10, 50, or 100 for each respectively, type *exit* if you want to quit.) \n")
        if choice == "10":
            inGame = True
            inMenu = False
            randomNumber = random.randint(1,10)
            while inGame:
                playerGuess = int(input("Guess a number from 1 to 10: "))
                if playerGuess == randomNumber:
                    print("You guessed the number!")
                    inMenu = True
                    inGame = False
                elif playerGuess != randomNumber:
                    print("Sorry, that's not the number!")
                    goToMenu = input("Do you want to go to menu? (type 'yes' or 'no') \n")
                    if goToMenu == "yes":
                        inGame = False
                        inMenu = True
        elif choice == "50":
            inGame = True
            inMenu = False
            randomNumber = random.randint(1,50)
            while inGame:
                playerGuess = int(input("Guess a number from 1 to 10: "))
                if playerGuess == randomNumber:
                    print("You guessed the number!")
                    inMenu = True
                    inGame = False
                elif playerGuess != randomNumber:
                    print("Sorry, that's not the number!")
                    goToMenu = input("Do you want to go to menu? (type 'yes' or 'no') \n")
                    if goToMenu == "yes":
                        inGame = False
                        inMenu = True
        elif choice == "100":
            inGame = True
            inMenu = False
            randomNumber = random.randint(1,100)
            while inGame:
                playerGuess = int(input("Guess a number from 1 to 10: "))
                if playerGuess == randomNumber:
                    print("You guessed the number!")
                    inMenu = True
                    inGame = False
                elif playerGuess != randomNumber:
                    print("Sorry, that's not the number!")
                    goToMenu = input("Do you want to go to menu? (type 'yes' or 'no') \n")
                    if goToMenu == "yes":
                        inGame = False
                        inMenu = True
    if detonatorGaming == "no":
        exit()

