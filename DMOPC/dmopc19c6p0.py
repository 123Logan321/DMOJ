import sys
numbers = list(map(int, sys.stdin.readline().split()))
i = 0
if numbers[0] < (numbers[1] + numbers[2]):

    if numbers[1] < (numbers[0] + numbers[2]):

        if numbers[2] < (numbers[1] + numbers[0]):
            print('yes')
            i += 1
if i == 0:
    print('no')
