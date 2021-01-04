import sys
days = int(sys.stdin.readline())
tasks = []
dp = []
for i in range(days):
    tasks.append(list(map(int, sys.stdin.readline().split())))

dp = tasks.copy()

for i in range(3):
    tasks.append([0,0,0])
    dp.append([0,0,0])

for i in range(1, days + 1):
    a = max(tasks[i - 1][1] + tasks[i][0], tasks[i - 1][2] + tasks[i][0])
    dp[i][0] = a
    b = max(tasks[i - 1][0] + tasks[i][1], tasks[i - 1][2] + tasks[i][1])
    dp[i][1] = b
    c = max(tasks[i - 1][0] + tasks[i][2], tasks[i - 1][1] + tasks[i][2])
    dp[i][2] = c

print(max(dp[days - 1]))

