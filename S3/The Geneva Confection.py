import sys
n_case = int(sys.stdin.readline())
for i in range(n_case):
    n_cars = int(sys.stdin.readline())
    car_order = []
    for x in range(n_cars):
        car_order.append(sys.stdin.readline())
    car_order.reverse()
    end = False
    starting = 1
    branch = []
    while len(car_order) != 0:
        if int(car_order[0]) == starting:
            del car_order[0]
            starting += 1
        else:
            if len(branch) != 0 and int(branch[-1]) == starting:
                del branch[-1]
                starting += 1
            else:
                branch.append(car_order[0])
                del car_order[0]
    if len(branch) == 0:
        print("Y")
    else:
        for i in range(len(branch)):    
            if int(branch[-1]) == starting:
                del branch[-1]
                starting += 1
            else:
                break
        if starting >= n_cars:
            print("Y")
        else:
            print("N")


                

