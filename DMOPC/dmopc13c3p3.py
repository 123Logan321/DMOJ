s = str(input()).split()
grid = []
grid1 = []
steps = [[1,0],[-1,0],[0,1],[0,-1]]
step_list = []
for i in range(int(s[0])):
    col = []
    grid1 = str(input()).split()
    grid.append(grid1)
    for x in range(int(s[0])):
        col.append(10000000000)
    step_list.append(col)
feed_list = [[0,0]]
start = [[0,0]]
step_list[0][0] = 0
while len(feed_list) != 0:
    cur_x = feed_list[0][0]
    cur_y = feed_list[0][1]
    feed_list.pop(0)
    for p in range(len(steps)):
        if (cur_x + steps[p][0] >= 0 and cur_x + steps[p][0] < int(s[0]) and cur_y + steps[p][1] >= 0 and cur_y + steps[p][1] < int(s[0])):
            if int(grid[cur_x][cur_y]) - int(grid[cur_x + steps[p][0]][cur_y + steps[p][1]]) >= (int(s[1])* - 1) and int(grid[cur_x][cur_y]) - int(grid[cur_x + steps[p][0]][cur_y + steps[p][1]]) <= int(s[1]):
                if step_list[cur_x + steps[p][0]][cur_y + steps[p][1]] > step_list[cur_x][cur_y] + 1:
                    step_list[cur_x + steps[p][0]][cur_y + steps[p][1]] = step_list[cur_x][cur_y] + 1
                    feed_list.append([cur_x + steps[p][0],cur_y + steps[p][1]])
if step_list[int(s[0]) - 1][int(s[0]) - 1] != 10000000000:
    print ("yes")
else:
    print ("no")