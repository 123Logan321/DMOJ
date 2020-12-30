spike = int(input())
space = int(input())
space1 = space * 2 + 3
bigbar = int(input())

repeat = 0
bar = 0
while repeat < spike:
    print ('*'+' '* space +"*"+' '* space+'*')
    repeat = repeat + 1
    
print ('*'* space1)
while bar < bigbar:
    print (' '* (space + 1)+'*' )
    bar = bar + 1
