nouns = int(input())
tings = int(input())
describe = []
objects = []
for i in range(nouns):
    describe += [input()]
for i in range(tings):
    objects += [input()]
for i in range(len(describe)):
    for p in range(len(objects)):
        print(describe[i],'as',objects[p])
