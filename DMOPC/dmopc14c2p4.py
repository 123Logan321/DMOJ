import sys
N_Q = int(sys.stdin.readline())
ep = []
for i in range(N_Q):
    ep.append(sys.stdin.readline().rstrip())

ps = []
ps.append(0)
for i in range(0, len(ep)):
    ps.append(int(ep[i]) + int(ps[i]))

x = int(sys.stdin.readline())
for i in range(x):
    s, e = list(map(int, sys.stdin.readline().split()))
    print(ps[e + 1] - ps[s])
    