import sys
s = [[1,0],[-1,0],[0,1],[0,-1]]
t = int(sys.stdin.readline())
h = int(sys.stdin.readline())
w = int(sys.stdin.readline())
floor = []
rooms = []
for i in range(h):
    floor.append(list(sys.stdin.readline()))

for row in range(h):
    for col in range(w):
        if floor[row][col] == '.':
            n = 1
            queue = []
            queue.append([row, col])
            while len(queue) != 0:
                r = queue[0][0]
                c = queue[0][1]
                floor[r][c] = 'I'
                queue.pop(0)
                for i in range(4):
                    if (r + s[i][0] >= 0) and (r + s[i][0] < h):
                        if (c + s[i][1] >= 0) and (c + s[i][1] < w):
                            if floor[r + s[i][0]][c + s[i][1]] == '.':
                                queue.append([(r + s[i][0]), (c + s[i][1])])
                                floor[r + s[i][0]][c + s[i][1]] = 'I'
                                n += 1
            rooms.append(n)
r = 0
rooms.sort(key=int, reverse=True)
for i in range(len(rooms)):
    if t - rooms[i] >= 0:
        t -= rooms[i]
        r += 1
    else:
        break

if r == 1:
    print('1 room,', str(t), 'square metre(s) left over')
else:
    print(str(r), 'rooms,', str(t), 'square metre(s) left over')
    


            
                

            
                
