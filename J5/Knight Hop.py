start = list(input())
target = list(input())
step_list = list()
for i in range(8):
    col = []
    for i in range(8):
        col.append(2147483647)
    step_list.append(col)
startx = int(start[0]) - 1
starty = int(start[-1]) - 1
targetx = int(target[0]) - 1
targety = int(target[-1]) - 1
feeder_listx = list()
feeder_listy = list()
feeder_listx.append(startx)
feeder_listy.append(starty)
#step_list is an array that contains each coordinate, and each element in it represents the coordinate, and start at 2147483647.
step_list[startx][starty] = 0
while len(feeder_listy) != 0:
    cur_x = feeder_listx[0] 
    cur_y = feeder_listy[0]
    del feeder_listx[0]
    del feeder_listy[0]
    if int(cur_x)+ 2 < 8 and int(cur_y) + 1 < 8 and int(step_list[cur_x][cur_y]) + 1 < step_list[int(cur_x)+ 2][int(cur_y) + 1]:
        feeder_listx.append(int(cur_x) + 2)
        feeder_listy.append(int(cur_y) + 1)
        step_list[int(cur_x)+ 2][int(cur_y) + 1] = step_list[cur_x][cur_y] + 1
    
    if int(cur_x)+ 1 < 8 and int(cur_y) + 2 < 8 and int(step_list[cur_x][cur_y]) + 1 < step_list[int(cur_x)+ 1][int(cur_y) + 2]:
        feeder_listx.append(int(cur_x) + 1)
        feeder_listy.append(int(cur_y) + 2)
        step_list[int(cur_x)+ 1][int(cur_y) + 2] = step_list[cur_x][cur_y] + 1

    if int(cur_x)- 1 >= 0 and int(cur_y) + 2 < 8 and int(step_list[cur_x][cur_y]) + 1 < step_list[int(cur_x)- 1][int(cur_y) + 2]:
        feeder_listx.append(int(cur_x) - 1)
        feeder_listy.append(int(cur_y) + 2)
        step_list[int(cur_x)- 1][int(cur_y) + 2] = step_list[cur_x][cur_y] + 1
    
    if int(cur_x)- 2 >= 0 and int(cur_y) + 1 < 8 and int(step_list[cur_x][cur_y]) + 1 < step_list[int(cur_x)- 2][int(cur_y) + 1]:
        feeder_listx.append(int(cur_x) - 2)
        feeder_listy.append(int(cur_y) + 1)
        step_list[int(cur_x)- 2][int(cur_y) + 1] = step_list[cur_x][cur_y] + 1
    
    if int(cur_x)- 1 >= 0 and int(cur_y) - 2 >= 0 and int(step_list[cur_x][cur_y]) + 1 < step_list[int(cur_x)- 1][int(cur_y) - 2]:
        feeder_listx.append(int(cur_x) - 1)
        feeder_listy.append(int(cur_y) - 2)
        step_list[int(cur_x)- 1][int(cur_y) - 2] = step_list[cur_x][cur_y] + 1
    
    if int(cur_x)- 2 >= 0 and int(cur_y) - 1 >= 0 and int(step_list[cur_x][cur_y]) + 1 < step_list[int(cur_x)- 2][int(cur_y) - 1]:
        feeder_listx.append(int(cur_x) - 2)
        feeder_listy.append(int(cur_y) - 1)
        step_list[int(cur_x)- 2][int(cur_y) - 1] = step_list[cur_x][cur_y] + 1
    
    if int(cur_x) + 1 < 8 and int(cur_y) - 2 >= 0 and int(step_list[cur_x][cur_y]) + 1 < step_list[int(cur_x)+ 1][int(cur_y) - 2]:
        feeder_listx.append(int(cur_x) + 1)
        feeder_listy.append(int(cur_y) - 2)
        step_list[int(cur_x) + 1][int(cur_y) - 2] = step_list[cur_x][cur_y] + 1
    
    if int(cur_x) + 2 < 8 and int(cur_y) - 1 >= 0 and int(step_list[cur_x][cur_y]) + 1 < step_list[int(cur_x)+ 2][int(cur_y) - 1]:
        feeder_listx.append(int(cur_x) + 2)
        feeder_listy.append(int(cur_y) - 1)
        step_list[int(cur_x) + 2][int(cur_y) - 1] = step_list[cur_x][cur_y] + 1

print (step_list[targetx][targety])
        