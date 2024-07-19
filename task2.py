m ='12345'
mid =len(m)//2
f= m[0:int(mid+1)]
s= m[int(mid+1):len(m)]
rev=''
for i in s:
        rev=i+rev
print(rev+f)
