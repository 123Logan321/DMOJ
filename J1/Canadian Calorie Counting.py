burger = int(input())
side = int(input())
drink = int(input())
dessert = int(input())

if burger == 1:
    burger = 461
elif burger == 2:
    burger = 431
elif burger == 3:
    burger = 420
elif burger == 4:
    burger = 0
    
if drink == 1:
    drink = 130
elif drink == 2:
    drink = 160
elif drink == 3:
    drink = 118
elif drink == 4:
    drink = 0
    
if side == 1:
    side = 100
elif side == 2:
    side = 57
elif side == 3:
    side = 70
elif side == 4:
    side = 0
    
if dessert == 1:
    dessert = 167
elif dessert == 2:
    dessert = 266
elif dessert == 3:
    dessert = 75
elif dessert == 4:
    dessert = 0

calories = burger + drink + side + dessert
print ("Your total Calorie count is %i." % (calories) )
