import sys
n = int(sys.stdin.readline())
number = []
for i in range(n):
    number.append(int(sys.stdin.readline()))
freq = []
for i in range(1001):
    freq.append(0)

for i in range(n):
    freq[number[i]] += 1

h = 1
hl = []
for i in range(len(freq)):
    if freq[i] >= h:
        h = freq[i]
h2 = 1
hl2 = []
for i in range(len(freq)):
    if freq[i] >= h2 and freq[i] < h:
        h2 = freq[i]
        
for i in range(len(freq)):
    if freq[i] == h:
        hl.append(i)
    elif freq[i] == h2:
        hl2.append(i)

if len(hl) >= 2:
    hl.sort(key=int)
    print(abs(hl[0] - hl[-1]))
else:
    hl2.sort(key=int)
    print(max(abs(hl2[0] - hl[0]),abs(hl2[-1] - hl[0])))



    



    




