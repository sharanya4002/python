n=5678
o=n
def single(n):
    ts=0
    while n>0:
        rem = n%10
        ts+= rem
        n//=10
        if n==0:
            n=ts
            print(n)
            if ts>10:
                ts=0
                continue
            else:
                return
single(o)
