friends = []
for i in range(50):
    col = []
    for x in range(50):
        col.append(0)
    friends.append(col)

friends[0][5] = 1
friends[5][0] = 1
friends[1][5] = 1
friends[5][1] = 1
friends[5][6] = 1
friends[6][5] = 1
friends[4][5] = 1
friends[5][4] = 1
friends[3][5] = 1
friends[5][3] = 1
friends[2][5] = 1
friends[5][2] = 1
friends[14][2] = 1
friends[2][14] = 1
friends[14][12] = 1
friends[12][14] = 1
friends[11][12] = 1
friends[12][11] = 1
friends[2][4] = 1
friends[4][2] = 1
friends[13][12] = 1
friends[12][13] = 1
friends[11][10] = 1
friends[10][11] = 1
friends[11][8] = 1
friends[8][11] = 1
friends[10][9] = 1
friends[9][10] = 1
friends[9][8] = 1
friends[8][9] = 1
friends[8][7] = 1
friends[7][8] = 1
friends[7][6] = 1
friends[6][7] = 1
friends[17][16] = 1
friends[16][17] = 1
friends[16][15] = 1
friends[15][16] = 1
friends[17][15] = 1
friends[15][17] = 1
friends[2][3] = 1
friends[3][2] = 1
friends[4][3] = 1
friends[3][4] = 1

end = False
while end == False:
    commands = input()
    if commands == 'q':
        end = True
    if commands == 'i':
        person1 = int(input())
        person2 = int(input())
        friends[person1 - 1][person2 - 1] = 1
        friends[person2 - 1][person1 - 1] = 1
    if commands == 'd':
        person1 = int(input())
        person2 = int(input())
        friends[person1 - 1][person2 - 1] = 0
        friends[person2 - 1][person1 - 1] = 0
    if commands == "n":
        person = int(input())
        number_of_friends = 0
        for i in range(len(friends)):
            if friends[person - 1][i] == 1:
                number_of_friends += 1
        print (number_of_friends)
    if commands == 's':
        start = int(input()) - 1
        target = int(input()) - 1
        feeder_list = list()
        feeder_list.append(start)
        steplist = list()
        for i in range(50):
            steplist.append(2147483647)
        #Feeder list
        #List of steps
        steplist[start] = 0
        while len(feeder_list) != 0:
            cur_friend = feeder_list[0]
            del feeder_list[0]
            for i in range(len(friends[cur_friend])):
                if friends[cur_friend][i] == 1 and steplist[cur_friend]+1 < steplist[i]:
                    feeder_list.append(i)
                    steplist[i] = steplist[cur_friend] + 1
        if steplist[target] == 2147483647:
            print ("Not connected")
        else:
            print (steplist[target])
        
    if commands == "f":
        '''
        1 = [0,1]
        2 = [1,0,1]
        3 = [0,1,0]  
        '''
        friends_of_friends = 0
        start = int(input()) - 1
        feeder_list = list()
        feeder_list.append(start)
        steplist = list()
        for i in range(50):
            steplist.append(2147483647)
        #Feeder list
        #List of steps
        steplist[start] = 0
        while len(feeder_list) != 0:
            cur_friend = feeder_list[0]
            del feeder_list[0]
            for i in range(len(friends[cur_friend])):
                if friends[cur_friend][i] == 1 and steplist[cur_friend]+1 < steplist[i]:
                    feeder_list.append(i)
                    steplist[i] = steplist[cur_friend] + 1
        for i in range(len(steplist)):
            if steplist[i] == 2:
                friends_of_friends += 1
        print (friends_of_friends)
            