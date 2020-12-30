import sys
s = [[1,0],[-1,0],[0,1],[0,-1]]
cases = int(sys.stdin.readline())
for i in range(cases):
    size = []
    layout = []
    start = []
    end = []
    step = []
    size.append((sys.stdin.readline()).split())
    for a in range(int(size[0][-1])):
        layout.append(list(sys.stdin.readline()))
        if "C" in list(layout[a]):
            start.append(a)
        if 'W' in list(layout[a]):
            end.append(a)
    for x in range(len(layout[start[0]])):
        if layout[start[0]][x] == 'C':
            start.append(x)
    for y in range(len(layout[end[0]])):
        if layout[end[0]][y] == 'W':
            end.append(y)
    queue = [[start[0], start[1]]]
    step = []
    for b in range(int(size[0][-1])):
        col = []
        for c in range(int(size[0][0])):
            col.append(10000000000000)
        step.append(col)
    step[int(start[0])][int(start[1])] = 0
    while len(queue) != 0:
        row = queue[0][0]
        col = queue[0][1]
        queue.pop(0)
        for i in range(4):
            if (int(row + s[i][0]) < int(size[0][-1])) and (int(col + s[i][-1]) < int(size[0][0])):
                if (row + s[i][0] >= 0) and (col + s[i][-1] >= 0):
                    if step[row][col] + 1 < step[row + s[i][0]][col + s[i][-1]]:
                        if layout[row + s[i][0]][col + s[i][-1]] == 'O' or layout[row + s[i][0]][col + s[i][-1]] == 'W':
                            step[row + s[i][0]][col + s[i][-1]] = step[row][col] + 1
                            queue.append([(row + s[i][0]), (col + s[i][-1])])
    if step[end[0]][end[1]] < 60:
        print(step[end[0]][end[1]])
    else:
        print("#notworth")

                
                
            

    
