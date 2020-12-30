#2,1,3,4,5,6,7
#1 < 7
#1 < 4
#2 < 1
#3 < 4
#3 < 5
import sys

prep = list()
task_manager = list()
for i in range(7):
    col = []
    prep.append(0)
    for i in range(7):
        col.append(0)
    task_manager.append(col)
task_manager[0][6] = 1
task_manager[0][3] = 1
task_manager[1][0] = 1
task_manager[2][3] = 1
task_manager[2][4] = 1
prep[6] += 1
prep[3] += 1
prep[0] += 1
prep[3] += 1
prep[4] += 1
end = False
order = list()
while end == False:
    x_command = int(sys.stdin.readline()) - 1
    y_command = int(sys.stdin.readline()) - 1
    if x_command == - 1 and y_command == - 1:
        end = True
    else:
        task_manager[x_command][y_command] = 1
        prep[y_command] += 1

for i in range(len(prep)):
    if prep[i] == 0:
        order.append(i)
order = sorted(order,key=int)


feed_list = list()
for i in range(len(order)):
    feed_list.append(order[i])
output = list()
while len(feed_list) != 0:
    cur_number = feed_list[0]
    output.append(int(feed_list[0]) + 1)
    del feed_list[0]
    for i in range(7):
        if task_manager[cur_number][i] == 1:
            prep[i] -= 1
            if prep[i] == 0:
                feed_list.append(i)
                feed_list = sorted(feed_list,key=int)


if len(output) == 7:
    output = " ".join(str(e) for e in (output))
    print (output)

else:
    print("Cannot complete these tasks. Going to bed.")

