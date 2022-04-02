import sys
num_of_test_cases = int(sys.stdin.readline())
for i in range(num_of_test_cases):
    test_case = int(sys.stdin.readline())
    end = False
    while end != True:
        test_case += 1
        if str(test_case)[-1] == '2':
            if str(test_case ** 3)[-3:] == '888':
                end = True
    print(test_case)