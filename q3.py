'''s='a1b2c3d492nm45'
for i in s:
    if  '0'<=i<='9':
        print(i,end='')
    else:
        continue
for i in s:    
    if  'a'<=i<='z':
        print(i,end='')
    else:
        continue'''

s='a1b2c3d492nm45'
m=''
n=''
for i in s:
    if i.isdigit():
        m+=i
    else:
        n+=i
print(m+n)

