n,k = map(int,  input().split(" "))
res = 0
score = list(map(int, input().split(" ")))
for i in range(n):
    if (score[k-1] ==0) and (score[i] == score[k-1]):
        res += 0 
    elif score[i] >= score[k-1]:
        res += 1
    else:
        res += 0 
print(res)

        

