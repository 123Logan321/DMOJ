decoded_sentence = list(input())
undecoded_sentence = list(input())
new_sentence = list(input())
final_sentence = list()
info_storage = {}
for i in range(len(decoded_sentence)):
    info_storage[undecoded_sentence[i]] = decoded_sentence[i]
for i in range(len(new_sentence)):
    if new_sentence[i] in info_storage.keys():
        final_sentence.append(info_storage[new_sentence[i]])
    else:
        final_sentence.append(".")

final_sentence = "".join(final_sentence)
print (final_sentence)