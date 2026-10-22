Strength = int(input("What's the strength stat of the ring? \n"))
Intelligence = int(input("What's the intelligence stat of the ring? \n"))
Dex = int(input("What's the dexterity stat of the ring? \n"))
damage = Strength * 2
magicPower = Intelligence
critChance = Dex/4

addStrength = int(input("How much is the ring getting upgraded in strength? \n"))
addIntelligence = int(input("How much is the ring getting upgraded in intelligence? \n"))
addDex = int(input("How much is the ring getting upgraded in dexterity? \n"))

truestrength = Strength + addStrength
trueintelligence = Intelligence + addIntelligence
truedex = Dex + addDex

superdamage = truestrength * 2
supermagicpower = trueintelligence
supercritchance = truedex * 0.25

print("Strength:")
print(Strength)
print("    + " + str(damage) + " Damage")

print("Intelligence:")
print(Intelligence)
print("    + " + str(magicPower) + " Magic Power")

print("Dexterity:")
print(Dex)
print("    + " + str(critChance) + " Crit Chance")

print("\n")
print("UPGRADED STATS:")
print("\n")

print("True Strength:")
print(truestrength)
print("    + " + str(superdamage) + " Super Damage")

print("True Intelligence:")
print(trueintelligence)
print("    + " + str(supermagicpower) + " Super Magic Power")

print("True Dexterity:")
print(truedex)
print("    + " + str(supercritchance) + "xxxer Crit Chance")