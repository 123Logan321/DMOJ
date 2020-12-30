Antenna = int(input())
Eyes = int(input())
if Antenna <= 2:
    if Eyes <= 3 and Eyes > 1:
        print ("VladSaturnian")
        print ("GraemeMercurian")
    if Eyes < 2:
        print ("GraemeMercurian")
    elif Eyes > 3:
        print ("VladSaturnian")
elif Antenna > 2:
    if Eyes <=4 and Eyes >= 2 and Antenna <= 6:
        print ("TroyMartian")
        print ('VladSaturnian')
    elif Eyes > 2 and Antenna <= 6:
        print ("VladSaturnian")
    elif Eyes <= 4:
        print ("TroyMartian")