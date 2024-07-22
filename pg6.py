n=int(input())
arr=list(map(int,input().split(" ")))
votcou = {}
for i in arr:
    if i in votcou:
        votcou[i] += 1
    else:
        votcou[i]=1
print(*votcou.items())
newArr = list(votcou.items())
print(newArr)
newArr.sort(key = lambda ele: ele[1])
print(newArr)
if newArr[-1]>newArr[-2]:
    print(newArr[-1])
else:
    print(-1)
        
