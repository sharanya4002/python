n=int(input())
def sonnum(n):
    if n==1:
        return 1
    else:
        return n+sonnum(n-1)
print(sonnum(n))
