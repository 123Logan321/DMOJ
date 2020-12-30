import sys

m = [[1,0],[0,1],[0,-1]]
size = int(sys.stdin.readline())
grid = []
for i in range(size):
    grid.append(list(input()))
queue = [[0,0]]
step_list = []
for i in range(size):
    col = []
    for i in range(size):
        col.append(10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
    step_list.append(col)
D = 0
R = 0
L = 0
step_list[0][0] = 0
while len(queue) != 0:
    cur_x = queue[0][0]
    cur_y = queue[0][1]
    queue.pop(0)
    for i in range(len(m)):
        if (cur_x + m[i][0]) >= 0 and (cur_x + m[i][0]) < size:
            if (cur_y + m[i][1]) >= 0 and (cur_y +m[i][1]) < size:
                if grid[cur_x + m[i][0]][cur_y + m[i][1]] == ".":
                    if step_list[cur_x][cur_y] + 1 < step_list[cur_x + m[i][0]][cur_y+m[i][1]]:
                        step_list[cur_x + m[i][0]][cur_y + m[i][1]] = step_list[cur_x][cur_y] + 1
                        queue.append([cur_x+m[i][0],cur_y+m[i][1]])
final = 0
L = ((step_list[size-1][size-1]) - 2*(size - 1)) / 2
D = size - 1
R = size - 1 + L
final = D**2 + R**2 + L**2
if step_list[size-1][size-1] != 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000:
    print (int(final))
else:
    print (int(-1))

