import sys
m = int(sys.stdin.readline())
q = int(sys.stdin.readline())
people = {}
name = []
pos = 0
for i in range(q):
    pos += 1
    name.append(sys.stdin.readline())
    time = int(sys.stdin.readline())
    people[str(name)] = time
print()

