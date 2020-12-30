useless = input()
String = input()
substring1 = 'A'
substring2 = "B"
countA = String.count(substring1)
countB = String.count(substring2)
if countA > countB:
    print ("A")
if countA < countB:
    print ("B")
if countA == countB:
    print ("Tie")