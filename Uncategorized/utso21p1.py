#1:2
#2:5 (3)
#3:8 (3)
#4:13 (5)
#5:18 (5)
#6:25
import sys
Rsize = 1
limit = 2
a = 3

r = int(sys.stdin.readline())

end = False
while end != True:
    for i in range(2):
        if r <= limit:
            print(Rsize)
            end = True
            break
        else:
            Rsize += 1
            limit += a
    if end == False:
        a += 2


