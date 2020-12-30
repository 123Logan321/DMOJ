score_a = 0
score_a += int(input())* 3
score_a += int(input())* 2
score_a += int(input())
score_b = 0
score_b += int(input())* 3
score_b += int(input())* 2
score_b += int(input())
if score_a > score_b:
    print("A")
elif score_a < score_b:
    print ("B")
else:
    print ("T")