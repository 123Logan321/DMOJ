def encode(message):
    encoded_m = []
    number_m = []
    for i in range(len(message)):
        number_m.append(list(str(len(message[i]))))
        encoded_m.append(list(message[i]))

    final_m = []
    final_word = ()
    end = False
    for i in range(len(number_m)):
        final_word = 
    return(message)


def decode(message):

    return(message)


for i in range(10):
    task = ()
    line = ()
    for i in range(2):
        task = input()
        line = input()
        line = line.split(" ")
        if task == "encode":
            print(encode(line))
        else:
            print(decode(line))
