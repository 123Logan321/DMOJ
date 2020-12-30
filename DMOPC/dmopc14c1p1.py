import math
cases = int(input())
numbers = []
for i in range(cases):
    numbers.append(input())
numbers.sort(key=int)
if len(numbers) % 2 == 0:
    x = int(len(numbers) / 2) - 1
    y = (int(int(numbers[x]) + int(numbers[x + 1])) / 2)
    if y - 0.5 == round(y):
        print (int(y + 0.5))
    else:
        print(round(y))
    
else:
    x = math.floor(int(len(numbers)) / 2)
    print(numbers[x])