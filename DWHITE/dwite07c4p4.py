possible_movements = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[1,-1],[-1,1] ,[-1,-1]]
for i in range(5):
    maze_array = []
    for i in range(10):
        col = []
        for i in range(10):
            col.append(0)
        maze_array.append(col)
    start = list()
    end = list()
    maze = list()
    for x in range(11):
        maze.append(list(input()))
    del maze[10]
    for y in range(10):
        for z in range(10):
            if maze[y][z] == ".":
                maze_array[y][z] = 1
            elif maze[y][z] == "X":
                maze_array[y][z] = 1
                start.append(y)
                start.append(z)
    step_list = list()
    for a in range(10):
        col = []
        for b in range(10):
            col.append(100000000000000)
        step_list.append(col)
    starty = int(start[0])
    startx = int(start[1])
    targety = int(start[2])
    targetx = int(start[3])
    feeder_list = list()
    feeder_list.append([starty,startx])
    step_list[starty][startx] = 0
    while len(feeder_list) != 0:
        cur_y = feeder_list[0][0]
        cur_x = feeder_list[0][1]
        feeder_list.pop(0)
        for j in range(len(possible_movements)):
            if (cur_y + possible_movements[j][0] >= 0 and cur_y + possible_movements[j][0] <= 9 and cur_x + possible_movements[j][1] >= 0 and cur_x + possible_movements[j][1] <= 9):
                if maze_array[cur_y + possible_movements[j][0]][cur_x + possible_movements[j][1]] == 1:
                    if step_list[cur_y + possible_movements[j][0]][cur_x + possible_movements[j][1]] > step_list[cur_y][cur_x] + 1:
                        step_list[cur_y + possible_movements[j][0]][cur_x + possible_movements[j][1]] = step_list[cur_y][cur_x] + 1
                        feeder_list.append([cur_y + possible_movements[j][0],cur_x + possible_movements[j][1]])

    print (step_list[targety][targetx])
