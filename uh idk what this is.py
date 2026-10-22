import random
import time

# Define color codes for printing
# These codes force the console to print in a certain color
class Color:
    RED = '\033[31m'
    GREEN = '\033[32m'
    BLUE = '\033[34m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m' # Resets all formatting

playerOneMoney = 1000
playerTwoMoney = 1000
inPlay = True
p1validBet = False
p2validBet = False
playerOneBet = 0
playerTwoBet = 0

# this is a 'function' that we create
# we can 'call' upon this function to 'roll' dice for us
def roll_dice_visually(amount):
    roll = 0
    print("ROLLING THE DICE ...")
    for i in range(amount):
        roll = random.randint(1, 6) # roll a random number
        time.sleep(0.1) # pause for 0.1 seconds
        print(roll, end=",") # print that roll visually, making sure no NEWLINE (\n) is added
    print("\n DICE LANDED ON: " + str(roll))
    return roll


playersConsent = str(input("Do you guys want to try your luck? Say ONLY *yes* if you want to go through. \n"))

if playersConsent .lower() == "yes":
    inPlay = True
else:
    inPlay = False

while inPlay:
    if not p1validBet:
        playerOneBet = int(input("Player One: What will your bet be? You have: $" + str(playerOneMoney) + "\n"))
        if playerOneBet > playerOneMoney:
            while playerOneBet > playerOneMoney:
                print("Player One Cannot Bet That Much!")
                playerOneBet = int(input("Player One: What will your bet be? \n"))
        else:
            p1validBet = True
    if not p2validBet:
        playerTwoBet = int(input("Player Two: What will your bet be? You have: $" + str(playerTwoMoney) + "\n"))
        if playerTwoBet > playerTwoMoney:
            while playerTwoBet > playerTwoMoney:
                print("Player Two Cannot Bet That Much!")
                playerTwoBet = int(input("Player Two: What will your bet be? \n"))
        else:
            p2validBet = True

    print("<------------------------->")
    playerOneRoll = roll_dice_visually(20) # here we CALL upon our custom function
    print("<------------------------->")

    print(f"{Color.RED} PLAYER 1 ROLLED: {playerOneRoll} {Color.RESET}")
    print("<------------------------->")

    print("<------------------------->")
    playerTwoRoll = roll_dice_visually(20) # here we CALL upon our custom function

    print("<------------------------->")
    print(f"{Color.GREEN} PLAYER 2 ROLLED: {playerTwoRoll} {Color.RESET}")
    print("<------------------------->")


    if playerOneRoll > playerTwoRoll:
        print("Player One Won!")
        playerOneMoney += playerTwoBet #it says it CAN be undefined
        playerTwoMoney -= playerTwoBet

        print("Player One has $" + str(playerOneMoney))
        if playerTwoMoney == 0:
            print("Player Two has no money! Player One WINS!!!")
            inPlay = False
        else:
            playersConsent = input("Do you want to try your luck again?")
            if playersConsent .lower() != "yes":
                print("Aw man, come back soon!")
                inPlay = False

    elif playerTwoRoll > playerOneRoll:
        print("Player Two Won!")
        playerTwoMoney += playerOneBet
        playerOneMoney -= playerOneBet

        print("Player Two has $" + str(playerTwoMoney))
        if playerOneMoney == 0:
            print("Player One has no money! Player Two WINS!!!")
            inPlay = False
        else:
            playersConsent = input("Do you want to try your luck again?")
            if playersConsent .lower() != "yes":
                print("Aw man, come back soon!")
                inPlay = False
    elif playerOneRoll == playerTwoRoll:
        playerOneDecision = input("Player One: Do you want to reroll or double down? You have: $" + str(playerOneMoney) + "\n")

        if playerOneDecision .lower() == "double down":
            playerOneBet *= 2
            if playerOneBet > playerOneMoney:
                print("Player One Cannot Bet That Much!")
                playerOneBet /= 2
            else:
                print("Player One has doubled down! Bet:" + str(playerOneBet))

        playerTwoDecision = input("Player Two: Do you want to reroll or double down? You have: $" + str(playerTwoMoney) + "\n")
        if playerTwoDecision .lower()=="double down":
            playerTwoBet *= 2
            if playerTwoBet > playerTwoMoney:
                print("Player Two Cannot Bet That Much!")
                playerTwoBet /= 2
            else:
                print("Player Two has doubled down! Bet:" + str(playerTwoBet))

        if playerOneDecision and playerTwoDecision .lower() == "reroll":
            print("REROLL:")
            playerOneBet = ""
            playerTwoBet = ""
            inPlay = True
        elif playerOneDecision.lower() == "double down" and playerTwoDecision.lower() == "double down":
            print("DOUBLING DOWN P1 and P2:")
            p1validBet = True
            p2validBet = True
        elif playerOneDecision .lower() == "double down":
            print("DOUBLING DOWN P1:")
            p1validBet = True
        elif playerTwoDecision.lower() == "double down":
            print("DOUBLING DOWN P2:")
            p2validBet = True
