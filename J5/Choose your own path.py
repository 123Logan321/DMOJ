number_of_pages = int(input())
book = list()
for i in range(number_of_pages):
        book.append(input().split())
        del book[i][0]
feeder_list = list()
feeder_list.append(0)
step_list = list()
for i in range(number_of_pages):
    step_list.append(2147483647)
step_list[0] = 1
while len(feeder_list) != 0:
    cur_number = feeder_list[0]
    del feeder_list[0]
    for i in range(len(book[cur_number])):
        if len(book[cur_number]) != 0 and step_list[cur_number] + 1 < step_list[int(book[cur_number][i]) - 1]:
            feeder_list.append(int(book[cur_number][i]) - 1)
            step_list[int(book[cur_number][i]) - 1] = step_list[cur_number] + 1
        elif len(book[cur_number]) == 0 and step_list[cur_number] + 1 < step_list[int(book[cur_number][i]) - 1]:
            step_list[int(book[cur_number][i]) - 1] = step_list[cur_number] + 1
            

yes = 0
for i in range(len(step_list)):
    if step_list[i] == 2147483647:
        yes += 1
        break
if yes > 0:
    print("N")
else:
    print("Y")

end_steps = list()
for i in range(number_of_pages):
    if  step_list[i] < 2147483647 and len(book[i]) == 0:
        end_steps.append(step_list[i])
end_steps = sorted(end_steps,key=int)
print (end_steps[0])