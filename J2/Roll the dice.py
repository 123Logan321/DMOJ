FirstDice = int(input())
SecondDice = int(input())
FirstSides = []
SecondSides = []
ways = 0
for i in range(1,FirstDice+1):
    FirstSides.append(i)
for i in range(1,SecondDice+1):
    SecondSides.append(i)
for i in (FirstSides):
    for x in (SecondSides):
        if int(i + SecondSides[x-1]) == 10:
            ways += 1

if ways == 1:
    print ("There is",(ways),"way to get the sum 10.")

else:
    print("There are",(ways),"ways to get the sum 10.")
