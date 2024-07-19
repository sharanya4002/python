#slicing
arr=[1,2,3,4,5]
k=4
first=arr[k-1:]
second=arr[:k-1]
print(first+second)
print("---------")
k=3
first=arr[k+1:k-(k-1):-1]
second=arr[:k-1]
print(first+second)
print("--------")
k=2
first=arr[:k+1]
second=arr[k+2:k:-1]
print(second+first)
#43215
k=3
first=arr[k::-1]
second=arr[k+1:]
print(first+second)

#54321
k=4
print(arr[k::-1])

