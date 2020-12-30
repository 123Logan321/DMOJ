Sumac1 = input()
Sumac2 = input()

num = 0

difference = list()
difference.append(Sumac1)
difference.append(Sumac2)

finallist = difference.copy()

while int(difference[-2]) - int(difference[-1]) >= 0:
    num = int(difference[-2]) - int(difference[-1])
    difference.append(num)
    finallist.append(num)

print(len(difference))