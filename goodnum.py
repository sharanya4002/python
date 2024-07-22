#good numbers--->res=low cube +high cube
import math
arr=[35,9,1]
c=0
for i in arr:
    low=1
    high=math.ceil(math.pow(i,1/3))
    while low<high:
        res=low**3+ high**3
        if res==i:
            c+=1
        if res<i:
            low+=1
        else:
            high-=1
    print(i)
print(c)



        
    
