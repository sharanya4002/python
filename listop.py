n=[ 'su','li','ar','rv','vk','mk']
n.pop()
n.pop(-1)
n.remove('rv')
n.append('dm')
n.insert(0,'sk')
n[1]='bv'
count=1
print(n)
print(n[True])
for ele in n:
    print(count,'-->',ele)
    count+=1
for i in range(0,len(n)):
    if (i%2)==0:
        print(n[i])
print('---------')

for i in range(0,len(n)):
    if (i%2)==0:
        rev=n[i]
        print(rev[::-1])
    else:
        print(n[i])


