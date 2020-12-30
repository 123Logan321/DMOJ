Text = input()
Stringsad = (":-(")
Stringhappy = (":-)")
countS = Text.count(Stringsad)
countB = Text.count(Stringhappy)
if countS == countB and countS != 0 and countB != 0:
    print ("unsure")

elif countS > countB:
    print ("sad")

elif countS < countB:
    print ("happy")

elif countS == 0 and countB == 0:
    print ("none")