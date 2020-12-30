A1 = int(input())
A2 = int(input())
A3 = int(input())
if A1 + A2 + A3 == 180:
    
    if A1 == A2 == A3:
        print ("Equilateral")
        
    elif A1 != A2 and A1 != A3 and A2 != A3:
        print ("Scalene")
       
    else:
        print ("Isosceles")
    
else:
    print("Error")