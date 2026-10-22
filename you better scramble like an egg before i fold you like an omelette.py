scramble1 = {"a":"d","b":"e","c":"f","d":"g","e":"h","f":"i","g":"j","h":"k","i":"l","j":"m","k":"n","l":"o","m":"p","n":"q","o":"r","p":"s","q":"t","r":"u","s":"v","t":"w","u":"x","v":"y","w":"z","x":"a","y":"b","z":"c", " ":" "}
scramble2 = {"a":"z","b":"y","c":"x","d":"w","e":"v","f":"u","g":"t","h":"s","i":"r","j":"q","k":"p","l":"o","m":"n","n":"m","o":"l","p":"k","q":"j","r":"i","s":"h","t":"g","u":"f","v":"e","w":"d","x":"c","y":"b","z":"a", " ":" "}

unscramble1 = {d:a for a,d in scramble1.items()}
unscramble2 = {z:a for a,z in scramble2.items()}

playerWord = input("What word would you like to use? \n").lower()

playerChoice = input("Scramble or Unscramble? \n")
if playerChoice.lower() == "scramble":
    playerScramble = input("Do you want to do the first or second scramble? (type 1 or 2) \n")
    if playerScramble == "1":
        for letter in playerWord:
            print(scramble1[letter], end = "")
    elif playerScramble == "2":
        for letter in playerWord:
            print(scramble2[letter], end = "")
elif playerChoice.lower() == "unscramble":
    playerUnscramble = input("Do you want to unscramble a scrambled word of the 1st type or 2nd type? (type 1 or 2) \n")
    if playerUnscramble == "1":
        for letter in playerWord:
            print(unscramble1[letter], end = "")
    elif playerUnscramble == "2":
        for letter in playerWord:
            print(unscramble2[letter], end = "")
