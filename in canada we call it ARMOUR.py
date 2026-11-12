import random

upgradeSlots = 7
armour = 3
magicDef = 1
hp = 14

print("Welcome! If you want to upgrade that leather tunic you have there, you'll need to purchase some upgrade scrolls.")
print("As it so happens, I have some right here. Each scroll takes up an upgrade slot, even if it fails. Be warned!")
print("The lower the chance of the scroll to work, the better the boost. Choose wisely!")
print(f"\nYour armour's current stats are: \nArmour = {armour}, \nMagic Defence = {magicDef}, \nHP = {hp}, \nUpgrade Slots = {upgradeSlots}")
while upgradeSlots > 0:
    upgradeScrollType = input(" \nWhich part of the leather tunic would you like to upgrade? Type: \n'armour' for armour, \n'magicdefence' for magic defence, or \n'hp' for HP.\n")
    if upgradeScrollType.lower() == 'armour':
        upgradeScrollRank = input("What rank of armour would you like to use? Type: \n'1' for the 10% chance for 4 armour, \n'2' for the 30% chance for 3 armour, or \n'3' for the 60% chance for 2 armour.\n")
        if upgradeScrollRank == "1":
            success = random.randint(1, 10)
            if success == 1:
                armour += 4
                upgradeSlots -= 1
                print("You have successfully upgraded!")
                print(
                    f"Your armour's new stats are: \nArmour = {armour}, \nMagic Defence = {magicDef}, \nHP = {hp}, \nUpgrade Slots = {upgradeSlots}")
            else:
                upgradeSlots -= 1
                print("Aw man, it failed! Miserably. Quite horrendously actually.")
                print(f"Your armour's stats are: \nArmour = {armour}, \nMagic Defence = {magicDef}, \nHP = {hp}, \nUpgrade Slots = {upgradeSlots}")
        elif upgradeScrollRank == "2":
            success = random.randint(1, 10)
            if success <= 3:
                armour += 3
                upgradeSlots -= 1
                print("You have successfully upgraded!")
                print(
                    f"Your armour's new stats are: \nArmour = {armour}, \nMagic Defence = {magicDef}, \nHP = {hp}, \nUpgrade Slots = {upgradeSlots}")
            else:
                upgradeSlots -= 1
                print("Aw man, it failed! Miserably. Quite horrendously actually.")
                print(
                    f"Your armour's stats are: \nArmour = {armour}, \nMagic Defence = {magicDef}, \nHP = {hp}, \nUpgrade Slots = {upgradeSlots}")
        elif upgradeScrollRank == "3":
            success = random.randint(1, 10)
            if success <= 6:
                armour += 2
                upgradeSlots -= 1
                print("You have successfully upgraded!")
                print(
                    f"Your armour's new stats are: \nArmour = {armour}, \nMagic Defence = {magicDef}, \nHP = {hp}, \nUpgrade Slots = {upgradeSlots}")
            else:
                upgradeSlots -= 1
                print("Aw man, it failed! Miserably. Quite horrendously actually.")
                print(
                    f"Your armour's stats are: \nArmour = {armour}, \nMagic Defence = {magicDef}, \nHP = {hp}, \nUpgrade Slots = {upgradeSlots}")
        else:
            print("That's not a real scroll, is it?")
    elif upgradeScrollType.lower() == 'magicdefence':
        upgradeScrollRank = input("What rank of magic defence would you like to use? Type: \n'1' for the 10% chance for 3 magic defence, \n'2' for the 30% chance for 2 magic defence, or \n'3' for the 60% chance for 1 magic defence.\n")
        if upgradeScrollRank == "1":
            success = random.randint(1, 10)
            if success == 1:
                magicDef += 3
                upgradeSlots -= 1
                print("You have successfully upgraded!")
                print(
                    f"Your armour's new stats are: \nArmour = {armour}, \nMagic Defence = {magicDef}, \nHP = {hp}, \nUpgrade Slots = {upgradeSlots}")
            else:
                upgradeSlots -= 1
                print("Aw man, it failed! Miserably. Quite horrendously actually.")
                print(
                    f"Your armour's stats are: \nArmour = {armour}, \nMagic Defence = {magicDef}, \nHP = {hp}, \nUpgrade Slots = {upgradeSlots}")
        elif upgradeScrollRank == "2":
            success = random.randint(1, 10)
            if success <= 3:
                magicDef += 2
                upgradeSlots -= 1
                print("You have successfully upgraded!")
                print(
                    f"Your armour's new stats are: \nArmour = {armour}, \nMagic Defence = {magicDef}, \nHP = {hp}, \nUpgrade Slots = {upgradeSlots}")
            else:
                upgradeSlots -= 1
                print("Aw man, it failed! Miserably. Quite horrendously actually.")
                print(
                    f"Your armour's stats are: \nArmour = {armour}, \nMagic Defence = {magicDef}, \nHP = {hp}, \nUpgrade Slots = {upgradeSlots}")
        elif upgradeScrollRank == "3":
            success = random.randint(1, 10)
            if success <= 6:
                magicDef += 1
                upgradeSlots -= 1
                print("You have successfully upgraded!")
                print(
                    f"Your armour's new stats are: \nArmour = {armour}, \nMagic Defence = {magicDef}, \nHP = {hp}, \nUpgrade Slots = {upgradeSlots}")
            else:
                upgradeSlots -= 1
                print("Aw man, it failed! Miserably. Quite horrendously actually.")
                print(
                    f"Your armour's stats are: \nArmour = {armour}, \nMagic Defence = {magicDef}, \nHP = {hp}, \nUpgrade Slots = {upgradeSlots}")
        else:
            print("That's not a real scroll, is it?")
    elif upgradeScrollType.lower() == 'hp':
        upgradeScrollRank = input(
            "What rank of HP would you like to use? Type: \n'1' for the 10% chance for 8 HP, \n'2' for the 30% chance for 4 HP, or \n'3' for the 60% chance for 2 HP.\n")
        if upgradeScrollRank == "1":
            success = random.randint(1, 10)
            if success == 1:
                hp += 8
                upgradeSlots -= 1
                print("You have successfully upgraded!")
                print(
                    f"Your armour's new stats are: \nArmour = {armour}, \nMagic Defence = {magicDef}, \nHP = {hp}, \nUpgrade Slots = {upgradeSlots}")
            else:
                upgradeSlots -= 1
                print("Aw man, it failed! Miserably. Quite horrendously actually.")
                print(
                    f"Your armour's stats are: \nArmour = {armour}, \nMagic Defence = {magicDef}, \nHP = {hp}, \nUpgrade Slots = {upgradeSlots}")
        elif upgradeScrollRank == "2":
            success = random.randint(1, 10)
            if success <= 3:
                hp += 4
                upgradeSlots -= 1
                print("You have successfully upgraded!")
                print(
                    f"Your armour's new stats are: \nArmour = {armour}, \nMagic Defence = {magicDef}, \nHP = {hp}, \nUpgrade Slots = {upgradeSlots}")
            else:
                upgradeSlots -= 1
                print("Aw man, it failed! Miserably. Quite horrendously actually.")
                print(
                    f"Your armour's stats are: \nArmour = {armour}, \nMagic Defence = {magicDef}, \nHP = {hp}, \nUpgrade Slots = {upgradeSlots}")
        elif upgradeScrollRank == "3":
            success = random.randint(1, 10)
            if success <= 6:
                hp += 2
                upgradeSlots -= 1
                print("You have successfully upgraded!")
                print(
                    f"Your armour's new stats are: \nArmour = {armour}, \nMagic Defence = {magicDef}, \nHP = {hp}, \nUpgrade Slots = {upgradeSlots}")
            else:
                upgradeSlots -= 1
                print("Aw man, it failed! Miserably. Quite horrendously actually.")
                print(
                    f"Your armour's stats are: \nArmour = {armour}, \nMagic Defence = {magicDef}, \nHP = {hp}, \nUpgrade Slots = {upgradeSlots}")
        else:
            print("That's not a real scroll, is it?")
    elif upgradeScrollType.lower() == 'armor':
        print("Buddy, we're not in America. This is Canada, and we add the U's. Try again.")
    elif upgradeScrollType.lower() == 'magicdefense':
        print("Buddy, we're not in America. This is Canada, and we have a C in our defenCe. Try again.")
    else:
        print(f"Ah yes, my favorite trait of armour...'{upgradeScrollType}'? Choose a real armour trait, buddy.")

print("\nWell that seems to be all the upgrades you can perform on that leather tunic.")
if armour == 3 and magicDef == 1 and hp == 14:
    print("...")
    print("It didn't even upgrade at all...")
    print("Are you sure you want to go on this journey?")
else:
    print("Good luck on your journey!")