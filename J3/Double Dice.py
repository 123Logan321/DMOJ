rounds = int(input())
scoreStore = []
firstEntry = 0
secondEntry = 0
team1 = 100
team2 = 100
for i in range(rounds):
  scoreStore += input()
  del scoreStore[1]
  firstEntry += int(scoreStore[0])
  secondEntry += int(scoreStore[1])
  if firstEntry > secondEntry:
    team2 -= firstEntry
  elif firstEntry < secondEntry:
    team1 -= secondEntry
  del scoreStore[0:len(scoreStore)]
  firstEntry = 0
  secondEntry = 0
print (team1)
print (team2)