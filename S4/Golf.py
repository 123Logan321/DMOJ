import sys
d = int(sys.stdin.readline())
n_clubs = int(sys.stdin.readline())
clubs = []
for i in range(n_clubs):
    clubs.append(int(sys.stdin.readline()))

clubs.sort(key=int,reverse=True)
dp = [0]
for i in range(1, d + 1):
    dp.append(10000000000000)
    for x in range(len(clubs)):
        if (i - clubs[x]) < 0:
            continue
        dp[i] = min(dp[i], dp[(i - clubs[x])] + 1)

if dp[d] == 10000000000000:
    print("Roberta acknowledges defeat.")

else:
    print("Roberta wins in " + str(dp[d]) + " strokes.")
