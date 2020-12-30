question = int(input())
citizens = int(input())
speed = 0
Dmo = []
Peg = []
if question == 1:
    Dmo = input().split(" ")
    Peg = input().split(" ")
    Dmo = sorted(Dmo,key=int)
    Peg = sorted(Peg,key=int)
    for i in range(len(Dmo)):
        if int(Dmo[i]) > int(Peg[i]):
            speed += int(Dmo[i])
        else:
            speed += int(Peg[i])
    print(speed)
elif question == 2:
    Dmo = input().split(" ")
    Peg = input().split(" ")
    Dmo = sorted(Dmo,key=int,reverse=True)
    Peg = sorted(Peg,key=int)
    for i in range(len(Dmo)):
        if int(Dmo[i]) > int(Peg[i]):
            speed += int(Dmo[i])
        else:
            speed += int(Peg[i])
    print(speed)