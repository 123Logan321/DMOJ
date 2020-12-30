FirstYear = int(input())
SecondYear = int(input())
Between = SecondYear - FirstYear
posChange = FirstYear
print ('All positions change in year',posChange)
for i in range(Between // 60):
    posChange += 60
    print ('All positions change in year',posChange)