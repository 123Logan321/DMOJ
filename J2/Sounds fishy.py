F1 = int(input())
F2 = int(input())
F3 = int(input())
F4 = int(input())
if F1 < F2 and F2 < F3 and F3 < F4:
    print ("Fish Rising")

elif F1 > F2 and F2 > F3 and F3 > F4:
    print ("Fish Diving")

elif F1 == F2 and F2 == F3 and F3 == F4:
    print ('Fish At Constant Depth')

else:
    print ('No Fish')