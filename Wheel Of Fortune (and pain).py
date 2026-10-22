import random
import time

words = ["credit", "tiptoe", "lean", "galaxy", "plant", "paralyzed", "bus", "nomination", "relative", "history", "sum", "girlfriend", "utter", "complain", "write", "tribe", "lover", "insistence", "wedding", "garlic"]
randomWord = random.choice(words)

vowels = ["a","e","i","o","u"]

guessList = []
guessedLetters = []

wordGuessed = False

for letter in randomWord:
    guessList.append("_ ")

for letter in guessList:
    print(letter, end = "")
print("\nThere are " + str(len(randomWord)) + " letters in the word. \n")

p1cash = 1000
p2cash = 1000

p1turn = True
p2turn = False

def roll_dice_visually(amount):
    roll = 0
    print("Spinning the Wheel Of Fortune...")
    for i in range(amount):
        roll = random.randint(0, 10) # roll a random number
        time.sleep(0.1) # pause for 0.1 seconds
        print(roll, end=",") # print that roll visually, making sure no NEWLINE (\n) is added
    return roll

while not wordGuessed:
    if p1turn:
        print("Player 1: You have $" + str(p1cash))
        p1choice = input("Player 1: Would you like to \n 1) buy a vowel for $200; \n 2) buy a consonant for $100; \n 3) spin the wheel; \n 4) guess the word. (input 1, 2, 3, or 4 for your choice) \n")
#----------------------------------------------------------------------------------------------
        if p1choice == "1":
            inValid = False
            while not inValid:
                if p1cash >= 200:
                    p1cash -= 200
                    p1vowelguess = input("Which vowel do you want to buy? (a,e,i,o,u) \n").lower()
                    if p1vowelguess in vowels:
                        if p1vowelguess not in guessedLetters:
                            guessedLetters.append(p1vowelguess)
                            for i in range(0, len(guessList)):
                                if randomWord[i] == p1vowelguess:
                                    guessList[i] = p1vowelguess + " "
                                else:
                                    pass
                            print("Guessed letters:")
                            for letter in guessedLetters:
                                print(letter, end=", ")
                            print("\n")

                            for letter in guessList:
                                print(letter, end="")
                            print("\n")
                            print("Player 1: You have $" + str(p1cash) + " left.\n")
                            p1turn = False
                            p2turn = True
                            inValid = True
                        else:
                            print("That has already been guessed!")
                            print("I gave you a list and everything!")
                            print("HOW CAN YOU STILL GUESS IT!!! >:O")
                            print("Just for your stupidity, I'm keeping the money >:D")
                    else:
                        print("That is not a vowel! >:(")
                        print("You still lose the money XD")

                else:
                    print("You don't have enough money!")
                    inValid = True
                    p1turn = True
                    p2turn = False
#----------------------------------------------------------------------------------------------
        if p1choice == "2":
            inValid = False
            while not inValid:
                if p1cash >= 100:
                    p1cash -= 100
                    p1CONguess = input("Which consonant do you want to buy? \n").lower()
                    if p1CONguess not in vowels and p1CONguess.isalpha():
                        if p1CONguess not in guessedLetters:
                            guessedLetters.append(p1CONguess)
                            for i in range(0, len(guessList)):
                                if randomWord[i] == p1CONguess:
                                    guessList[i] = p1CONguess + " "
                                else:
                                    pass
                            print("Guessed letters:")
                            for letter in guessedLetters:
                                print(letter, end=", ")
                            print("\n")

                            for letter in guessList:
                                print(letter, end="")
                            print("\n")
                            print("Player 1: You have $" + str(p1cash) + " left. \n")
                            p1turn = False
                            p2turn = True
                            inValid = True
                        else:
                            print("That has already been guessed!")
                            print("I gave you a list and everything!")
                            print("HOW CAN YOU STILL GUESS IT!!! >:O")
                            print("Just for your stupidity, I'm keeping the money >:D")
                    else:
                        print("That is not a consonant! >:(")
                        print("You still lose the money XD")
                else:
                    print("You don't have enough money!")
                    inValid = True
                    p1turn = True
                    p2turn = False
# ----------------------------------------------------------------------------------------------
        if p1choice == "3":
            p1roll = int(roll_dice_visually(15))
            if p1roll == 0:
                print("Oh no! You rolled BANKRUPT!")
                p1cash = 0
                print("Player 1: You have no cash! \n")
            else:
                p1gains = p1roll * 100
                print("\n You rolled $" + str(p1gains) + "!")
                p1cash += p1gains
                print("Player 1: You have $" + str(p1cash) + "! \n")

            print("Guessed letters:")
            for letter in guessedLetters:
                print(letter, end=", ")
            print("\n")

            for letter in guessList:
                print(letter, end="")
            print("\n")
            p1turn = False
            p2turn = True
# ----------------------------------------------------------------------------------------------
        if p1choice == "4":
            p1WordGuess = input("What do you think the word is?").lower()
            if p1WordGuess == randomWord:
                print("Player 1 guessed the word!")
                print("Player 1 has WON!")
                wordGuessed = True
            else:
                print("Sorry, that's not the word.")

                print("Guessed letters:")
                for letter in guessedLetters:
                    print(letter, end=", ")
                print("\n")

                for letter in guessList:
                    print(letter, end="")
                print("\n")
                p1turn = False
                p2turn = True
#############################################################################################
#############################################################################################
    elif p2turn:
        print("Player 2: You have $" + str(p2cash))
        p2choice = input("Player 2: Would you like to \n 1) buy a vowel for $200; \n 2) buy a consonant for $100; \n 3) spin the wheel; \n 4) guess the word. (input 1, 2, 3, or 4 for your choice) \n")
#----------------------------------------------------------------------------------------------
        if p2choice == "1":
            inValid = False
            while not inValid:
                if p2cash >= 200:
                    p2cash -= 200
                    p2vowelguess = input("Which vowel do you want to buy? (a,e,i,o,u)").lower()
                    if p2vowelguess in vowels:
                        if p2vowelguess not in guessedLetters:
                            guessedLetters.append(p2vowelguess)
                            for i in range(0, len(guessList)):
                                if randomWord[i] == p2vowelguess:
                                    guessList[i] = p2vowelguess + " "
                                else:
                                    pass
                            print("Guessed letters:")
                            for letter in guessedLetters:
                                print(letter, end=", ")
                            print("\n")

                            for letter in guessList:
                                print(letter, end="")
                            print("\n")
                            print("Player 2: You have $" + str(p2cash) + " left. \n")
                            p1turn = True
                            p2turn = False
                            inValid = True
                        else:
                            print("That has already been guessed!")
                            print("I gave you a list and everything!")
                            print("HOW CAN YOU STILL GUESS IT!!! >:O")
                            print("Just for your stupidity, I'm keeping the money >:D")
                    else:
                        print("That is not a vowel! >:(")
                        print("You still lose the money XD")
                else:
                    print("You don't have enough money!")
                    inValid = True
                    p1turn = False
                    p2turn = True
#----------------------------------------------------------------------------------------------
        if p2choice == "2":
            inValid = False
            while not inValid:
                if p2cash >= 100:
                    p2cash -= 100
                    p2CONguess = input("Which consonant do you want to buy?").lower()
                    if p2CONguess not in vowels and p2CONguess.isalpha():
                        if p2CONguess not in guessedLetters:
                            guessedLetters.append(p2CONguess)
                            for i in range(0, len(guessList)):
                                if randomWord[i] == p2CONguess:
                                    guessList[i] = p2CONguess + " "
                                else:
                                    pass
                            print("Guessed letters:")
                            for letter in guessedLetters:
                                print(letter, end=", ")
                            print("\n")

                            for letter in guessList:
                                print(letter, end="")
                            print("\n")
                            print("Player 2: You have $" + str(p2cash) + " left. \n")
                            p1turn = True
                            p2turn = False
                        else:
                            print("That has already been guessed!")
                            print("I gave you a list and everything!")
                            print("HOW CAN YOU STILL GUESS IT!!! >:O")
                            print("Just for your stupidity, I'm keeping the money >:D")
                    else:
                        print("That is not a consonant! >:(")
                        print("You still lose the money XD")
                else:
                    print("You don't have enough money!")
                    inValid = True
                    p1turn = False
                    p2turn = True
# ----------------------------------------------------------------------------------------------
        if p2choice == "3":
            p2roll = int(roll_dice_visually(15))
            if p2roll == 0:
                print("Oh no! You rolled BANKRUPT!")
                p2cash = 0
                print("Player 2: You have no cash! \n")
            else:
                p2gains = p2roll * 100
                print("\n You rolled $" + str(p2gains) + "!")
                p2cash += p2gains
                print("Player 2: You have $" + str(p2cash) + "! \n")

            print("Guessed letters:")
            for letter in guessedLetters:
                print(letter, end=", ")
            print("\n")

            for letter in guessList:
                print(letter, end="")
            print("\n")
            p1turn = True
            p2turn = False
# ----------------------------------------------------------------------------------------------
        if p2choice == "4":
            p2WordGuess = input("What do you think the word is?").lower()
            if p2WordGuess == randomWord:
                print("Player 2 guessed the word!")
                print("Player 2 has WON!")
                wordGuessed = True
            else:
                print("Sorry, that's not the word.")

                print("Guessed letters:")
                for letter in guessedLetters:
                    print(letter, end=", ")
                print("\n")

                for letter in guessList:
                    print(letter, end="")
                print("\n")
                p1turn = True
                p2turn = False