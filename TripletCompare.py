a = list(map(int, input().rstrip().split()))
b = list(map(int, input().rstrip().split()))
a_score = 0
b_score = 0

for i,j in zip(a,b):
    print('----',i,j)
    if i>j:
        a_score += 1
    elif j>i:
        b_score += 1
    else:
        a_score +=0
        b_score +=0

print(a_score,b_score)

        