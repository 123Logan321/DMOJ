top = int(input())
bottom = int(input())
whole = top // bottom
remaintop = top % bottom
divisors = list()

newtop = 0
newbottom = 0
for i in range(bottom):
    if i != 0 and top % i == 0 and bottom % i == 0:
        divisors.append(i)
divisors = sorted(divisors,key=int,reverse=True)
newtop = int(remaintop / divisors[0])
newbottom = int(bottom / divisors[0])

if remaintop == 0:
    print(whole)

elif whole != 0:
    print (whole,str(newtop)+"/"+str(newbottom))

elif whole == 0 and len(divisors) != 1:
    print (str(newtop)+"/"+str(newbottom))

else:
    print(str(top)+"/"+str(bottom))