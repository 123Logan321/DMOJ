end = False
instruction = []
while end != True:
    x = ()
    x = input()
    if x == 'SCHOOL':
        end = True
    else:
        instruction.append(x)
instruction.reverse()
instruction.append("HOME")
x = -1
y = 0
for i in range(int(len(instruction) / 2)):
    if instruction[y] == "R" and i != int(len(instruction) / 2) - 1:
        print ('Turn LEFT onto',instruction[x + 2],'street.')
        x += 2
        y += 2
    elif instruction[y] == "L" and i != int(len(instruction) / 2) - 1:
        print('Turn RIGHT onto',instruction[x + 2],'street.')
        x += 2
        y += 2
    elif instruction[y] == "L":
        print('Turn RIGHT into your',instruction[x + 2]+".")
    elif instruction[y] == "R":
        print('Turn LEFT into your',instruction[x + 2]+".")
