import sys
rows = int(sys.stdin.readline())
m = list(sys.stdin.readline())
graph = []
for i in range(2000):
    col = []
    for x in range(rows):
        col.append('.')
    graph.append(col)

start = [[999, 0]]
for i in range(rows):
    row = start[0][0] 
    col = start[0][1]
    start.pop(0)
    if m[i] == '^':
        graph[row][col] = '/'
        start.append([row - 1, col + 1])
    elif m[i] == 'v':
        graph[row + 1][col] = "\\"
        start.append([row + 1, col + 1])
    elif m[i] == '>':
        graph[row][col] = '_'
        start.append([row, col + 1])

for i in range(2000):
    if "\\" in graph[i] or '/' in graph[i] or "_" in graph[i]:
        print("".join(graph[i]))



    
                
                
            

    
