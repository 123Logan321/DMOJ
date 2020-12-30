number = int(input())
shift = int(input())
if shift == 0:
    print (number)

if shift == 1:
    print (number + number * 10)

if shift == 2:
    print (number + number * 10 + number * 100)

if shift == 3:
    print (number + number * 10 + number * 100 + number * 1000)

if shift == 4:
    print (number + number * 10 + number * 100 + number * 1000 + number * 10000)

if shift == 5:
    print (number + number * 10 + number * 100 + number * 1000 + number * 10000 + number * 100000)
