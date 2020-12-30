parks = int(input())
zuotian = []
today = []
spaces = 0
zuotian += input()
today += input()
for i in range(parks):
    if zuotian[i] == today[i]:
        if zuotian[i] == "C":
            spaces += 1
    else:
        None
print(spaces)
