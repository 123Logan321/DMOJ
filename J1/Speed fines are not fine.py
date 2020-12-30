Limit = int(input())
Speed = int(input())
if Speed <= Limit:
    print ("Congratulations, you are within the speed limit!")
elif Speed > Limit:
    Money = Speed - Limit
    if Money <= 20:
        print ("You are speeding and your fine is $100.")
    elif Money <= 30:
        print ("You are speeding and your fine is $270.")
    elif Money > 30:
        print ("You are speeding and your fine is $500.")
