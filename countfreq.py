#count frequency of elements of array
arr=[1,2,3,6,5,4,7,3,5,2,1]
count = 0
d={}
for key in arr:
     if key not in d:
         d[key]=1
     else:
         d[key]+=1
for  num,count in d.items():
    if count==1:
        print(num)
print("----------------")

for  num,count in d.items():
    if count>1:
        print(num)
