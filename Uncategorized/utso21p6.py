import sys
ncases = int(sys.stdin.readline())
for i in range(ncases):
    N_K = list(map(int, sys.stdin.readline().split()))
    hills = []
    d = []
    hills = (list(map(int, sys.stdin.readline().split())))
    for i in range(N_K[0]):
        if i == N_K[0] - 1:
            break
        else:
            d.append(abs(hills[i] - hills[i + 1]))
    d.sort(key=int, reverse=True)
    if N_K[1] != 0:
        print(d[1])
    else:
        print(d[0])
