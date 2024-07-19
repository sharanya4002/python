n=5
fact = 1
for i in range(1,n+1):
    fact *=i
print(fact)
print("-------------")
i=int(input())
def fact(i):

    if abs(i==0) or abs(i==1):
        return 1
    else:
        return i*fact(i-1)
print(fact(i))

