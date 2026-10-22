numList = []

for i in range(0,5):
    num = int(input(f"Enter number {i + 1}: "))
    numList.append(num)

averageNum = sum(numList)/len(numList)
sumNum = sum(numList)

print(f"Average of your numbers: {averageNum}")
print(f"Sum of all numbers: {sumNum}")