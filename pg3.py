jarsnum=int(input())
nofchoc= list(map(int,input().split(' ')))
a=0
b=0
c=0
list=[]
for i in range(len(nofchoc)):
    s=nofchoc[i]
    while(s>0):
        if(s!=0):
            a=1+a
            s=s-1
        if(s!=0):
            b=1+b
            s=s-1
        if(s!=0):
            c=1+c
            s=s-1
    list.append(a)
    a=0
    b=0
    c=0
print(sum(list))       
