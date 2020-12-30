questions = int(input())
student = []
answer = [] 
marks = 0
for i in range(questions):
  student += input()
for i in range(questions):
  answer += input()
for i in range(questions):
  if student[i] == answer[i]:
    marks += 1
print(marks)