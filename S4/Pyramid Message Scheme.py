import sys
test_cases = int(sys.stdin.readline()) 
for i in range(test_cases):
    connections = int(sys.stdin.readline())
    layout = []
    word_checker = []
    word = ()
    number = 0
    array = []
    for i in range(connections):
        layout.append(sys.stdin.readline().rstrip())
        col = []
        for i in range(connections):
            col.append(0)
        array.append(col)
    start = layout[-1]
    word_checker.append(start)
    for i in range(connections):
        if layout[i] == start:
            layout[i] = 0
    for i in range(connections):
        condition = True
        if str(layout[i]).isdigit() == False:
            for x in range(len(word_checker)):
                if str(layout[i]) == str(word_checker[x]):
                    condition = False
            if condition == True:
                number += 1
                word_checker.append(layout[i])
                word = layout[i]
                for i in range(connections):
                    if layout[i] == word:
                        layout[i] = number
    x = 0
    y = 0
    for i in range(int(len(layout) / 2)):
        array[layout[x]][layout[y+1]] = 1
        array[layout[y+1]][layout[x]] = 1
        x += 2
        y += 2
    queue = []
    queue.append(0)
    steps = []
    final = 0
    for i in range(connections):
        steps.append(10000000000000000000000000000)
    steps[0] = 0
    while len(queue) != 0:
        cur = queue[0]
        del queue[0]
        for i in range(connections):
            if array[cur][i] == 1 and steps[cur] + 1 < steps[i]:
                queue.append(i)
                steps[i] = steps[cur] + 1
                final += 20
    steps = sorted(steps,key=int,reverse=True)
    for i in range(len(steps)):
        if steps[i] != 10000000000000000000000000000:
            final = final - (steps[i]*20)
            break
    print(final)

