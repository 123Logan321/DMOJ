import sys
n = int(sys.stdin.readline())
l = []
for i in range(n):
    l.append(sys.stdin.readline())
l = list(map(int, l))
l.sort(key=int)
for i in range(len(l)):
    print(l[i])