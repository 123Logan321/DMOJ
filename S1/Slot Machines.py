import sys
q = int(sys.stdin.readline())
m = 1
m1 = int(sys.stdin.readline())
m2 = int(sys.stdin.readline())
m3 = int(sys.stdin.readline())
c = 0
while q != 0:
    c += 1
    q -= 1
    if m == 4:
        m = 1

    if m == 1:
        m1 += 1
        if m1 == 35:
            q += 30
            m1 = 0
        
    elif m == 2:
        m2 += 1
        if m2 == 100:
            q += 60
            m2 = 0

    else:
        m3 += 1
        if m3 == 10:
            q += 9
            m3 = 0

    m += 1

print("Martha plays", str(c) ,"times before going broke.")
    

