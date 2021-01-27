import sys
N_Q = sys.stdin.readline().split()
ep = sys.stdin.readline().split()

for i in range(0, len(ep)):
    ep[i] = int(ep[i])
p = [0]

for i in range(0, len(ep)):
    p.append(ep[i] + p[i])
f = p[len(p) - 1]

for i in range(int(N_Q[1])):
    s, e= list(map(int, sys.stdin.readline().split()))
    m = p[e] - p[s-1]
    print(f - m)

