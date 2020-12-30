letters = int(input())
bosscallouts = []
callouts = None
math = 0
for i in range(letters):
    callouts = int(input())
    if callouts == 0:
        del bosscallouts[len(bosscallouts) - 1]
    else:
        bosscallouts += [str(callouts)]
for i in range(len(bosscallouts)):
    math += int(bosscallouts[i])
print (math)