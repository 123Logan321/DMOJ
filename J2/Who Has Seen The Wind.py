h = int(input())
t = int(input())
A = 0
for i in range(1,t):
    if (-6*(i)**4+(h)*(i)**3+2*(i)**2+(i)) <= 0:
        print ("The balloon first touches ground at hour:")
        print (i)
        A += 1
        break

if A == 0:
    print ("The balloon does not touch ground in the given time.")

