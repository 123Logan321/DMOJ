import sys
r = int(sys.stdin.readline())
c = int(sys.stdin.readline())
row = []
room_layout = []
step = []
for i in range(r):
    room_layout.append(str(sys.stdin.readline()).split())
    col = []
    for x in range(c):
        col.append(1000000000)
    step.append(col)

queue = [[0,0]]
step[0][0] = 0
while len(queue) != 0:
    cur_x = queue[0][0]
    cur_y = queue[0][1]
    queue.pop(0)
    for i in range(1, int(room_layout[cur_x][cur_y]) + 1 ):
        if int(room_layout[cur_x][cur_y]) % i == 0:
            if i <= r and int(room_layout[cur_x][cur_y]) / i  <= c:
                if step[cur_x][cur_y] + 1 < step[i - 1][int(int(room_layout[cur_x][cur_y]) / i) - 1]:
                    if room_layout[cur_x][cur_y] != 1:
                        queue.append([int(int(i) - 1),(int(int(room_layout[cur_x][cur_y]) / i) -1)])
                        step[i - 1][int(int(room_layout[cur_x][cur_y]) / i) - 1] = step[cur_x][cur_y] + 1
    for x in range(r):
        for y in range(c):
            if room_layout[cur_x][cur_y] == room_layout[x][y]:
                room_layout[x][y] = 1
if step[r - 1][c - 1] != 1000000000:
    print ("yes")
else:
    print("no")


