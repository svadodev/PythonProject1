startNum = int(input("Enter the first number: "))
endNum = int(input("Enter the second number: "))

rangeNum = endNum - startNum - 1
if rangeNum < 0:
    rangeNum = rangeNum * -1



numList = []
oddList = []
evenList = []

for i in range(rangeNum):
    i = i + 1 + startNum
    numList.append(i)

for num in numList:
    oddOreven = num % 2
    if oddOreven == 0:
        evenList.append(num)
    elif oddOreven == 1:
        oddList.append(num)



evenSum = sum(evenList)
oddList = (', '.join(map(str, oddList)))
print(f"Sum of all even numbers between that range: {evenSum}")
print(f"All odd numbers in that range: {oddList}")



