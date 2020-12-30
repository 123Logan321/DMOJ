lines = int(input())
text = []
tCounter = 0
sCounter = 0
for i in range(lines):
    text += list(input().lower())
for i in range(len(text)):
    if 't' in text[i]:
        tCounter += 1
    elif 's' in text[i]:
        sCounter += 1
if tCounter > sCounter:
    print ('English')
else:
    print ('French')