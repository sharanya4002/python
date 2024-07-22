alice=[10,3,6]
bob=[12,3,7]
a,b=0,0
for i in range(len(alice)):
    if alice[i]>bob[i]:
        a+=1
    elif bob[i]>alice[i]:
        b+=1
print(max(a,b))
