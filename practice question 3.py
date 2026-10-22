f = open("names","r+")

lines = f.readlines()
noLines = len(lines)


will = input(f"Would you like to add a name to the list? Answer yes or no. Current amount of names in list: {noLines}. ")

if will.lower() == "yes":

    nameAdd = int(input("How many names would you like to add? "))

    for i in range(nameAdd):
        givenName = input(f"What name would you like to add? ")
        f.write(str(givenName))
        f.write("\n")
        noLines += 1


    print(f"The length of the name list is now {noLines}.")

else:
    print(f"Oh, okay. The length of the name list will remain at {noLines}.")

    for line in lines:
        print(f"Length of {line}: {len(line) -1}")