Month = int(input())
Day = int(input())
if Month <= 2 and Day < 18:
    print ("Before")

elif Month < 2:
    print ("Before")

elif Month >=2 and Day > 18:
    print ("After")

elif Month == 2 and Day == 18:
    print ("Special")

elif Month > 2:
    print ("After")