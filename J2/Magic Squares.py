rows = []
colums1 = []
colums2 = []
colums3 = []
colums4 = []
answer = []
for i in range(4):
    rows = input().split(' ')
    colums1.append(rows[0])
    colums2.append(rows[1])
    colums3.append(rows[2])
    colums4.append(rows[3])
    answer.append(int(rows[0])+int(rows[1])+int(rows[2])+int(rows[3]))
answer.append(int(colums4[0])+int(colums4[1])+int(colums4[2])+int(colums4[3]))
answer.append(int(colums1[0])+int(colums1[1])+int(colums1[2])+int(colums1[3]))
answer.append(int(colums2[0])+int(colums2[1])+int(colums2[2])+int(colums2[3]))
answer.append(int(colums3[0])+int(colums3[1])+int(colums3[2])+int(colums3[3]))
if all(x == answer[0] for x in answer):
    print('magic')
else:
    print('not magic')