fl = list('*x*')
sl = list(' xx')
tl = list('* *')

FL = []
SL = []
TL = []

size = int(input())
for f in fl:
    FL.append(f * size)
for s in sl:
    SL.append(s * size)
for t in tl:
    TL.append(t * size)
for i in range(size):
    print (''.join(FL))
for i in range(size):
    print (''.join(SL))
for i in range(size):
    print (''.join(TL))
