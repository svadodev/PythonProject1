import random

listNums = []
while len(listNums) < 100:
    randomNum = random.randint(1000,9999)
    listNums.append(randomNum)

winningNumber = random.choice(listNums)
loser = []

numContestants = int(input("How many contestants will waste their life earnings today?"))

contestantsResults = []

for i in range(0,numContestants):
    contestantDraw = random.choice(listNums)
    print(f"Contestant {i+1} drew: {contestantDraw}")
    contestantsResults.append(contestantDraw)

print(f"The winning number is {winningNumber}.")


for i in range(0,len(contestantsResults)):
    guessCheckCurrent = contestantsResults[i]
    if guessCheckCurrent == winningNumber:
        print(f"Contestant {i+1} wins!")
    else:
        loser.append(i)
if len(loser) == numContestants:
    print("Nobody won...")