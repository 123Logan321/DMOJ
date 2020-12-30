default = list('9780921418')
math = 0
for i in range(3):
    default += input()
for i in range(len(default)):
    if i % 2 == 1:
        math += (int(default[i]) * 3)
    else: 
        math += int(default[i])
print ('The 1-3-sum is',math)