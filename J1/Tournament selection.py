R1 = input()
R2 = input()
R3 = input()
R4 = input()
R5 = input()
R6 = input()
Round = (R1,R2,R3,R4,R5,R6)
stringW = "W"
countR = Round.count(stringW)
if countR >= 5:
    print ('1')

elif countR >= 3:
    print ('2')

elif countR >= 1:
    print ("3")

else:
    print ("-1")
