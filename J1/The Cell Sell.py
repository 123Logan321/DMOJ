import math
import decimal

daytime = int(input())
evening = int(input())
weekend = int(input())
if daytime < 100:
    daytime1 = 100
    daytime2 = 250
    
elif daytime <= 250 and daytime >= 100:
    daytime1 = daytime
    daytime2 = 250

else:
    daytime1 = daytime
    daytime2 = daytime
    
PlanA = (daytime1 - 100)*0.25 + (evening * 0.15) + (weekend * 0.2)
PlanB = (daytime2 - 250)*0.45 + (evening * 0.35) + (weekend * 0.25)
print ("Plan A costs %.2f"% (PlanA))
print ("Plan B costs %.2f"% (PlanB))

if PlanA < PlanB:
    print ("Plan A is cheapest.")

elif PlanB < PlanA:
    print ("Plan B is cheapest.")

else:
    print ("Plan A and B are the same price.")