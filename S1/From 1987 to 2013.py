year = int(input())
x = 0
indicate = 0
while x < 1:
    try:
        year += 1
        x = 0
        indicate = 0
        yearNumber = list(str(year))
        for i in range(len(yearNumber)):
            for y in range(len(yearNumber)):
                if i != y:
                    if yearNumber[i] == yearNumber[y]:
                        indicate += 1
                        break
                    
        if indicate > 0:
            continue
        else:
            x += 10
    except IndexError:
        continue
print (year)