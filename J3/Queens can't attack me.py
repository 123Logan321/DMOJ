info = input()
info = info.split(" ")
grid = list()

for i in range(int(info[0])):
    col = []
    for i in range(int(info[0])):
        col.append(0)
    grid.append(col)
for i in range(int(info[-1])):
    queen_position = input().split(" ")
    grid[int(queen_position[0]) - 1][int(queen_position[-1]) - 1] = 1
    for i in range(int(info[0])):
        grid[int(queen_position[0])- 1][i] = 1
        grid[i][int(queen_position[-1]) - 1] = 1
    
    queen_position[0] = int(queen_position[0]) - 1
    queen_position[-1] = int(queen_position[-1]) - 1
    end = False
    while end == False:
        for i in range(int(info[0])):
            if int(queen_position[0]) + i  < int(info[0]) and int(queen_position[-1]) + i < int(info[0]) and grid[int(queen_position[0]) + i ][int(queen_position[-1]) + i] != 1:
                grid[int(queen_position[0]) + i ][int(queen_position[-1]) + i] = 1
                
        for i in range(int(info[0])):
            if int(queen_position[0])+i < int(info[0]) and int(queen_position[-1])+i < int(info[0]):
                grid[int(queen_position[0]) + i][int(queen_position[-1]) + i] = 1

            if int(queen_position[0])+i < int(info[0]) and int(queen_position[-1])-i >= 0:
                grid[int(queen_position[0]) + i][int(queen_position[-1]) - i] = 1

            if int(queen_position[0])-i >= 0 and int(queen_position[-1])+i < int(info[0]):
                grid[int(queen_position[0])-i][int(queen_position[-1])+i] = 1
            
            if int(queen_position[0])-i >= 0 and int(queen_position[-1])-i >= 0:
                grid[int(queen_position[0])-i][int(queen_position[-1])-i] = 1

        end = True
counter = 0
for i in range(int(info[0])):
    for x in range(int(info[0])):
        if int(grid[i][x]) == 0:
            counter += 1

print(counter)