import re 

word = input()
RS = dict.fromkeys('IOSHZXN')

if all(x in RS for x in word):
    print('YES')
    
else:
    print('NO')