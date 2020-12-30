import sys
s = [[0,1],[0,-1],[1,0],[-1,0]]
for i in range(5):
    grid = []
    start = []
    steplist = []
    number = 0
    for x in range(11):
        grid.append(list(sys.stdin.readline()))
        if 'A' in grid[x]:
            for y in range(len(grid[x])):
                if grid[x][y] == 'A':
                    start = [x, y]
    for a in range(11):
        col = []
        for b in range(11):
            col.append(100000000000000000000000000)
        steplist.append(col)

    queue = [[start[0],start[1]]]
    steplist[start[0]][start[1]] = 0
    while len(queue) != 0:
        cur_x = queue[0][0]
        cur_y = queue[0][1]
        queue.pop(0)
        for i in range(4):
            if (cur_x + s[i][0]) < 10 and (cur_x + s[i][0]) >= 0:
                if (cur_y + s[i][1]) < 10 and (cur_y + s[i][1]) >= 0:
                    if grid[cur_x + s[i][0]][cur_y + s[i][1]] == '#':
                        if steplist[cur_x][cur_y] + 1 < steplist[cur_x + s[i][0]][cur_y + s[i][1]]:
                            queue.append([cur_x + s[i][0], cur_y + s[i][1]])
                            steplist[cur_x + s[i][0]][cur_y + s[i][1]] = steplist[cur_x][cur_y] + 1

    for c in range(11):
        for d in range(11):
            if steplist[c][d] != 100000000000000000000000000:
                number += 1
    print(number)