f = open("binary in","r+")
g = open("binary out","r+")

lines = f.readlines()
noOfLines = len(lines)


for line in lines:
    num = int(line)
    numList = []
    while num > 0:
        numRemainder = num % 2
        num = int(num / 2)
        numList.append(numRemainder)
    numList.reverse()
    g.write(str(numList))
    g.write("\n")
