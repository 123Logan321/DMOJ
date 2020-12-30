indicators = input()
indicators = indicators.split()
e = str()
train_map = []
for i in range(4):
    if i == 0:
        for i in range(int(indicators[0])):
            col = []
            for i in range(int(indicators[0])):
                col.append(0)
            train_map.append(col)
    elif i == 3:
        for i in range(int(indicators[-1])):
            e = input()
            e = e.split()
            train_map[int(e[0]) - 1][int(e[-1]) - 1] = 1
feed = list()
feed.append(int(indicators[1]) - 1)
step_list = list()

for i in range(int(indicators[0])):
    step_list.append(2147483647)
step_list[int(indicators[1]) - 1] = 0
while len(feed) != 0:
    cur_train = feed[0]
    del feed[0]
    for i in range(int(indicators[0])):
        if train_map[cur_train][i] == 1 and step_list[cur_train] + 1 < step_list[i]:
            feed.append(i)
            step_list[i] = step_list[cur_train] + 1
print (step_list[int(indicators[2]) - 1])