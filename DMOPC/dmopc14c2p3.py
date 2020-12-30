import sys
items = int(sys.stdin.readline())
l_log = []
l_energy = []
for i in range(1):
    l_log = (sys.stdin.readline().split())
    l_energy = (sys.stdin.readline().split())
    l_log = list(map(int, l_log))
    l_energy = list(map(int, l_energy))

l_log.sort(key=int, reverse=True)
l_energy.sort(key=int)
total = 0
for i in range(items):
    total = total + (int(l_log[i]) * int(l_energy[i]))
print(total)
    
                
 