container = []
orcheck = []
finallist = []
Type = None
while Type != "quit!":
    Type = input()
    if Type == 'quit!':
        None
    else:
        container.append(Type)
        orcheck += container[0]
        if len(orcheck) > 4:
            if orcheck[len(orcheck) - 1] == 'r' and orcheck[len(orcheck) - 2] == 'o' and orcheck[len(orcheck) - 3] not in ('a','e','i','o','u','y'):
                orcheck.insert(len(orcheck) - 1, 'u')
                finallist = "".join(orcheck)
                print (finallist)
                container.clear()
                orcheck.clear()
            else:
                print(container[0])
                container.clear()
                orcheck.clear()
                    
        else:
            print(container[0])
            container.clear()
            orcheck.clear()