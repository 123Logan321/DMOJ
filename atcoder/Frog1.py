import sys
n = int(sys.stdin.readline())
stones = list(map(int, sys.stdin.readline().split()))
dp = []
for i in range(n + 15):
    dp.append(69696969)
    stones.append(0)

dp[0] = 0
dp[1] = abs(stones[1]-stones[0])
for x in range(n):
    one_rock = abs(stones[x + 2] - stones[x + 1]) + dp[x + 1]
    two_rock = abs(stones[x + 2] - stones[x]) + dp[x]
    dp[x + 2] = min(one_rock, two_rock)

print(dp[n - 1])
