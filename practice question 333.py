truckCapacity = 1000


print("The truck can hold: " + str(truckCapacity) + " kgs \n")

amntMarble = float(input("Enter the amount of Banana Crates you want to ship: "))
if amntMarble < 0:
    print("We ARE NOT shipping ANTIbananas.")
    marbleNegative = True
    while marbleNegative:
        amntMarble = float(input("Enter the amount of Banana Crates you want to ship: "))
        if amntMarble < 0:
            print("I told you we ARE NOT shipping ANTIbananas!!!")
        elif amntMarble > 0:
            marbleNegative = False
marbleWeight = amntMarble * 6
print("This weighs: " + str(marbleWeight) + " kgs \n")

amntGranite = float(input("Enter the amount of Mango Crates you want to ship: "))
if amntGranite < 0:
    print("We ARE NOT shipping ANTImangos.")
    graniteNegative = True
    while graniteNegative:
        amntGranite = float(input("Enter the amount of Mango Crates you want to ship: "))
        if amntGranite < 0:
            print("I told you we ARE NOT shipping ANTImangos!!!")
        elif amntGranite > 0:
            graniteNegative = False
graniteWeight = amntGranite * 5
print("This weighs: " + str(graniteWeight) + " kgs \n")

amntTitanium = float(input("Enter the amount of Pineapple Crates you want to ship: "))
if amntTitanium < 0:
    print("We ARE NOT shipping ANTIpineapple.")
    titaniumNegative = True
    while titaniumNegative:
        amntTitanium = float(input("Enter the amount of Pineapple Crates you want to ship: "))
        if amntTitanium < 0:
            print("I told you we ARE NOT shipping ANTIpineapple!!!")
        elif amntTitanium > 0:
            titaniumNegative = False
titaniumWeight = amntTitanium * 8
print("This weighs: " + str(titaniumWeight) + " kgs \n")

amntSteel = float(input("Enter the amount of Orange Crates you want to ship: "))
if amntSteel < 0:
    print("We ARE NOT shipping ANTIoranges.")
    steelNegative = True
    while steelNegative:
        amntSteel = float(input("Enter the amount of Orange Crates you want to ship: "))
        if amntSteel < 0:
            print("I told you we ARE NOT shipping ANTIorange!!!")
        elif amntSteel > 0:
            steelNegative = False
steelWeight = amntSteel * 5
print("This weighs: " + str(steelWeight) + " kgs \n")

truckLoad = marbleWeight + graniteWeight + titaniumWeight + steelWeight
truckLeft = truckCapacity - truckLoad

print("You loaded: " + str(truckLoad) + " kgs")
print("The truck can store: " + str(truckCapacity) + " kgs")
if truckLeft > 0:
    if truckLoad := 0:
        print("The truck driver is not amused. >:(")
    else:
        print("The truck can ship off that much material!")
        print("There it goes!!! :)")
elif truckLeft < 0:
    print("The truck can not ship off that much material!")
    print("You have made enemies with the truck driver! >_<")
else:
    print("The truck can ship off that much material, with no room to spare!")
    print("The truck driver admires your resourcefulness as they drive off! B)")