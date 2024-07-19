n=int(input())
ori=n
sum=0
while n>0:
    rem=n%10
    sum+=rem
    n=n//10
print(sum)
d=sum
revsum=0
while sum>0:
    r=sum%10
    revsum=revsum*10+r
    sum=sum//10
print(revsum)
out=d*revsum
if ori==out:
    print("magical number")
else:
    print(" not a magical number")
