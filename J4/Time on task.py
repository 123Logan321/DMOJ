AvailTime = int(input())
numOfChores = int(input())
AvailChores = list()

final = 0
for i in range(numOfChores):
    AvailChores.append(int(input()))

AvailChores.sort(key=int)
for i in range(len(AvailChores)):
    if AvailTime - AvailChores[i] >= 0:
        final += 1
        AvailTime -= AvailChores[i]

print(final)