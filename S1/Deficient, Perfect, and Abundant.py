import sys
n = int(sys.stdin.readline())
for i in range(n):
    number = int(sys.stdin.readline())
    s = []
    t = 0
    for x in range(int(number // 2)):
        if number % (x + 1) == 0:
            s.append(x + 1)
    for y in range(len(s)):
        t += int(s[y])
    if t > number:
        print(number,'is an abundant number.')
    elif t < number:
        print(number,'is a deficient number.')
    else:
        print(number,'is a perfect number.' )
