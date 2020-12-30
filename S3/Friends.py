bonds = int(input())
r = {}
for i in range(bonds):
    f = str(input()).split()
    r[f[0]] = int(f[1])
end = False
while end != True:
    search = str(input()).split()
    if search[0] == '0' and search[0] == '0':
        end = True
    else:
        queue = []
        queue.append(search[0])
        step_list = []
        for i in range(0,10000):
            step_list.append(1000000000000000000000000000)
        step_list[int(search[0])] = -1
        while len(queue) != 0:
            cur_n = queue[0]
            del queue[0]
            if step_list[int(cur_n)] + 1 < step_list[r[str(cur_n)]]:
                step_list[r[str(cur_n)]] = step_list[int(cur_n)] + 1
                queue.append(r[str(cur_n)])
        if step_list[int(search[1])] == 1000000000000000000000000000:
            print ("No")
        else:
            print ("Yes",step_list[int(search[1])])