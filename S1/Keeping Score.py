dealt_cards = list(input())
dealt_cards_2 = dealt_cards.copy()
clubs = list()
diamonds = list()
hearts = list()
spades = list()
for i in range(len(dealt_cards)):
    if dealt_cards[0] != "D":
        if dealt_cards[0] != "C":
            clubs.append(dealt_cards[0])
        del dealt_cards[0]
    else:
        break

for i in range(len(dealt_cards)):
    if dealt_cards[0] != "H":
        if dealt_cards[0] != "D":
            diamonds.append(dealt_cards[0])
        del dealt_cards[0]
    else:
        break

for i in range(len(dealt_cards)):
    if dealt_cards[0] != "S":
        if dealt_cards[0] != "H":
            hearts.append(dealt_cards[0])
        del dealt_cards[0]
    else:
        break

for i in range(len(dealt_cards) - 1):
    spades.append(dealt_cards[i+1])

clubs_point = 0
diamonds_point = 0
hearts_point = 0
spades_point = 0

if len(clubs) == 0:
    clubs_point += 3
elif len(clubs) == 1:
    clubs_point += 2
elif len(clubs) == 2:
    clubs_point += 1
for i in range(len(clubs)):
    if clubs[i] == "J":
        clubs_point += 1
    elif clubs[i] == "Q":
        clubs_point += 2
    elif clubs[i] == "K":
        clubs_point += 3
    elif clubs[i] == "A":
        clubs_point += 4
        
if len(diamonds) == 0:
    diamonds_point += 3
elif len(diamonds) == 1:
    diamonds_point += 2
elif len(diamonds) == 2:
    diamonds_point += 1
for i in range(len(diamonds)):
    if diamonds[i] == "J":
        diamonds_point += 1
    elif diamonds[i] == "Q":
        diamonds_point += 2
    elif diamonds[i] == "K":
        diamonds_point += 3
    elif diamonds[i] == "A":
        diamonds_point += 4


if len(hearts) == 0:
    hearts_point += 3
elif len(hearts) == 1:
    hearts_point += 2
elif len(hearts) == 2:
    hearts_point += 1
for i in range(len(hearts)):
    if hearts[i] == "J":
        hearts_point += 1
    elif hearts[i] == "Q":
        hearts_point += 2
    elif hearts[i] == "K":
        hearts_point += 3
    elif hearts[i] == "A":
        hearts_point += 4

if len(spades) == 0:
    spades_point += 3
elif len(spades) == 1:
    spades_point += 2
elif len(spades) == 2:
    spades_point += 1
for i in range(len(spades)):
    if spades[i] == "J":
        spades_point += 1
    elif spades[i] == "Q":
        spades_point += 2
    elif spades[i] == "K":
        spades_point += 3
    elif spades[i] == "A":
        spades_point += 4

clubs = " ".join(clubs)
diamonds = " ".join(diamonds)
hearts = " ".join(hearts)
spades = " ".join(spades)
total_point = clubs_point + diamonds_point + hearts_point + spades_point
d = {"Clubs":[clubs,clubs_point],
"Diamonds":[diamonds,diamonds_point],
"Hearts":[hearts,hearts_point],
"Spades":[spades,spades_point]
}
cards = ()
dealt = ()
point = ()

print ("{:<8} {:<15} {:<10}".format('Cards','Dealt','Points'))
for k, v in d.items():
    dealt, point = v
    print ("{:<8} {:<15} {:<10}".format(k, dealt, point))
print ("Total",total_point)