import sys
c = int(sys.stdin.readline())
cP = []
nP = []
for i in range(c):
    a = list(map(int, sys.stdin.readline().split()))
    cP.append(int(a[0] * a[1]))
n = int(sys.stdin.readline())
for i in range(n):
    b = list(map(int, sys.stdin.readline().split()))
    nP.append(int(b[0] * b[1]))
cP.sort(key=int, reverse=True)
nP.sort(key=int, reverse=True)
if cP[0] > nP[0]:
    print("Casper")
elif cP[0] < nP[0]:
    print("Natalie")
else:
    print("Tie")
