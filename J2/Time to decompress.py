NumberOfLines = int(input())
for i in range(NumberOfLines):
    message = input()
    words = message.split()
    print (int(words[0])*words[-1])
