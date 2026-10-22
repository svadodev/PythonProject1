truckCapacity = 5000


print("The truck can hold: " + str(truckCapacity) + " kgs \n")

amntMarble = float(input("Enter the amount of marble slabs you want to ship: "))
if amntMarble < 0:
    print("We ARE NOT shipping ANTImarble.")
    marbleNegative = True
    while marbleNegative:
        amntMarble = float(input("Enter the amount of marble slabs you want to ship: "))
        if amntMarble < 0:
            print("I told you we ARE NOT shipping ANTImarble!!!")
        elif amntMarble > 0:
            marbleNegative = False
marbleWeight = amntMarble * 150
print("This weighs: " + str(marbleWeight) + " kgs \n")

amntGranite = float(input("Enter the amount of granite slabs you want to ship: "))
if amntGranite < 0:
    print("We ARE NOT shipping ANTIgranite.")
    graniteNegative = True
    while graniteNegative:
        amntGranite = float(input("Enter the amount of granite slabs you want to ship: "))
        if amntGranite < 0:
            print("I told you we ARE NOT shipping ANTIgranite!!!")
        elif amntGranite > 0:
            graniteNegative = False
graniteWeight = amntGranite * 200
print("This weighs: " + str(graniteWeight) + " kgs \n")

amntTitanium = float(input("Enter the amount of titanium slabs you want to ship: "))
if amntTitanium < 0:
    print("We ARE NOT shipping ANTItitanium.")
    titaniumNegative = True
    while titaniumNegative:
        amntTitanium = float(input("Enter the amount of titanium slabs you want to ship: "))
        if amntTitanium < 0:
            print("I told you we ARE NOT shipping ANTItitanium!!!")
        elif amntTitanium > 0:
            titaniumNegative = False
titaniumWeight = amntTitanium * 750
print("This weighs: " + str(titaniumWeight) + " kgs \n")

amntSteel = float(input("Enter the amount of steel slabs you want to ship: "))
if amntSteel < 0:
    print("We ARE NOT shipping ANTIsteel.")
    steelNegative = True
    while steelNegative:
        amntSteel = float(input("Enter the amount of steel slabs you want to ship: "))
        if amntSteel < 0:
            print("I told you we ARE NOT shipping ANTIsteel!!!")
        elif amntSteel > 0:
            steelNegative = False
steelWeight = amntSteel * 1000
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
    print("You have made enemies with the truck driver! -_-")
else:
    print("The truck can ship off that much material, with no room to spare!")
    print("The truck driver admires your resourcefulness as they drive off! B)")