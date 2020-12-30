amount_of_numbers = int(input())
factors = list()
decision = 0
for i in range(amount_of_numbers):
    integer = int(input())
    factors = list()
    decision = 0
    for i in range(1,integer + 1):
        if integer % i == 0:
            factors.append(i)
    end = False
    while end == False:
        if len(factors) < 3:
            end = True
        for i in range(int(len(factors)/2)):
            for x in range(int(len(factors)/2)):
                    if factors[0] + factors[-1] == factors[x+1] - factors[(x*-1)-2]:
                        decision += 1

                    elif factors[0] + factors[-1] == factors[(x*-1)-2] - factors[x+1]:
                        decision += 1

                    elif factors[0] - factors[-1] == factors[x+1] + factors[(x*-1)-2]:
                        decision += 1

                    elif factors[-1] - factors[0] == factors[x+1] + factors[(x*-1)-2]:
                        decision += 1

                    else:
                        continue

            del factors[0]
            del factors[-1]

    if decision != 0:
        print (integer, "is nasty")
    else:
        print (integer, "is not nasty")