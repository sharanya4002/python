'''n=int(input())
k=int(input())
arr= list(map(int,input().split(' ')))
ans=0
for i in range(n-k+1):
    sub_arr =(arr[i:i+k:1])
    sum =0
    for j in range(1,k+1):
        sum += sub_arr[j-1]*j
    if sum>ans:
        ans =sum
print(ans)'''
n= int(input())
k = int(input())
arr = list(map(int, input().split()))
dict = {}
for i in range(n - k + 1):
    sub_arr = arr[i:i + k]  
    sum = 0
    for j in range(k):
        sum += sub_arr[j] * (j + 1)     
    dict[i] = sum
maximum= max(dict.values())
print(maximum)

