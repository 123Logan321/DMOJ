end = False
available_roads = []
while end == False:
    road = ()
    road = input()
    if road == "**":
        end = True
    available_roads.append(road)
del available_roads[-1]
road_map = []
for i in range(26):
    col = []
    for i in range(26):
        col.append(0)
    road_map.append(col)
for i in range(len(available_roads)):
    xaxis = 0
    yaxis = 0   
    road_checker = []
    road_checker = available_roads[i]
    xaxis = ord(road_checker[0])
    yaxis = ord(road_checker[-1])
    xaxis -= 65
    yaxis -= 65
    road_map[xaxis][yaxis] = 1
    road_map[yaxis][xaxis] = 1

killable_roads = 0
for i in range(len(available_roads)):
    xaxis = 0
    yaxis = 0   
    road_checker = []
    road_checker = available_roads[i]
    xaxis = ord(road_checker[0])
    yaxis = ord(road_checker[-1])
    xaxis -= 65
    yaxis -= 65

    road_map[xaxis][yaxis] = 0
    road_map[yaxis][xaxis] = 0

    feeder_list = list()
    feeder_list.append(0)
    step_list = list()
    for i in range(26):
        step_list.append(2147483647)
    step_list[0] = 0
    while len(feeder_list) != 0:
        cur_tunnel = feeder_list[0]
        del feeder_list[0]
        for i in range(26):     
            if  road_map[cur_tunnel][i] == 1 and step_list[i] == 2147483647:
                feeder_list.append(i)
                step_list[i] = step_list[cur_tunnel] + 1
    if step_list[1] == 2147483647:
        print(road_checker)
        killable_roads += 1
    road_map[xaxis][yaxis] = 1
    road_map[yaxis][xaxis] = 1

if killable_roads > 0:
    print ("There are",killable_roads,"disconnecting roads.")
else:
    print ("There are 0 disconnecting roads.")


    