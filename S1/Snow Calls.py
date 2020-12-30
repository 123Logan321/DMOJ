import sys
cases = int(sys.stdin.readline())
for i in range(cases):
    case = []
    f = []
    case = list(sys.stdin.readline().rstrip())
    x = 0
    while len(f) < 10:
        if case[x] == '-':
            x += 1
            continue
        else:
            if case[x] == 'A'or case[x] == 'B' or case[x] == 'C':
                f.append('2')
            elif case[x] == 'D'or case[x] == 'E' or case[x] == 'F':
                f.append('3')
            elif case[x] == 'G'or case[x] == 'H' or case[x] == 'I':
                f.append('4')
            elif case[x] == 'J'or case[x] == 'K' or case[x] == 'L':
                f.append('5')
            elif case[x] == 'M'or case[x] == 'N' or case[x] == 'O':
                f.append('6')
            elif case[x] == 'P'or case[x] == 'Q' or case[x] == 'R' or case[x] == 'S':
                f.append('7')
            elif case[x] == 'V'or case[x] == 'T' or case[x] == 'U':
                f.append('8')
            elif case[x] == 'W' or case[x] == 'X' or case[x] == 'Y' or case[x] == 'Z':
                f.append('9')
            else:
                f.append(case[x])
            x += 1
    f.insert(3,'-')
    f.insert(7,'-')
    print(''.join(f))
