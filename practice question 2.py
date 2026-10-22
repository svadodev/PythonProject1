numList = []

for i in range(4):
    num = int(input(f"Enter number {i+1}: "))
    numList.append(num)

firstNum = numList[0] + numList[1]
if numList[2] > numList[3]:
    secondNum = numList[2] - numList[3]
else:
    secondNum = numList[3] - numList[2]

finalNum = firstNum * secondNum

print(f"\nFirst number: {firstNum}")
print(f"Second number: {secondNum}")
print(f"Final number: {finalNum}")