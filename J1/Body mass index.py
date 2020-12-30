import math
import decimal
Weight = input()
Height = input()

BMIH =  decimal.Decimal(Height) * decimal.Decimal(Height)
BMI = decimal.Decimal(Weight) / (BMIH)

if BMI < decimal.Decimal(18.5):
    print ("Underweight")
    
elif BMI > 25:
    print ("Overweight")

elif BMI >= decimal.Decimal(18.5) and BMI <= 25:
    print ("Normal weight")