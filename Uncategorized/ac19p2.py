import sys
l = int(sys.stdin.readline())
s = int(sys.stdin.readline())
letter = sys.stdin.readline()
letter2 = []
c = []
a = list('abcdefghijklmnopqrstuvwxyz')
d = {}
for i in range(1, 27):
    d[str(i)] = (a[i - 1])
s = s % 26

for x in letter:
    if x == ' ':
        letter2.append(' ')
    else:    
        for y in range(len(a)):
            if a[y] == x and (y + 1 + s) <= 26:
                letter2.append(y + 1 + s)
                break

            elif a[y] == x:
                letter2.append(s - (26 - (y + 1)))
                break

            else:
                continue

for i in letter2:
    if i == ' ':
        c.append(' ')
    else:
        c.append(d.get(str(i)))
c = "".join(c)
print(str(c))
