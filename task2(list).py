arr = [ 1,2,3,4,5]
k=4
first=arr[k-1:]
second=arr[:k-1]
print(first+second)
print(first.extend(second))
