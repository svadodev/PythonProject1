itemAmount = int(input("Enter the amount of items you want to buy: "))
taxPercentage = int(input("Enter the tax percentage: "))

fruitValues = {"orange": 1, "banana": 2, "apple": 1.5, "pear" : 1.65, "kiwi": 1.74, "watermelon": 3.45}
listFruits = []

for i in range(itemAmount):
    item = input("What's item #" + str(i + 1) + "? No capital letters. \n")
    listFruits.append(fruitValues[item])

fruitSum = sum(listFruits)
finalPrice = fruitSum + (taxPercentage / 100) * fruitSum
realFinalPrice = round(finalPrice, 2)
print("$" + str(realFinalPrice))


