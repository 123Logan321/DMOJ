NumberOfLines = int(input())
theSymbols = list()
minilist = list()
symbols = str()
Variable = ()
numbers = 1
final = list()
for i in range(NumberOfLines):
    symbols = input()
    theSymbols.append(symbols)
    minilist = str(theSymbols[i])
    for i in range(len(minilist)):
        Variable = minilist[i]
        if i+1 < len(minilist) and Variable == minilist[i+1]:
            numbers += 1
        else:
            final += str(numbers) +" "+Variable+" "
            numbers = 1
    print (str("".join(final)))
    final = list()
