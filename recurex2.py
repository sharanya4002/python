#finding nTh element in fibnocci series
n=int(input())
def fib(n):
    if n==0 or n==1:
        return n
    else:
        return fib(n-1)+fib(n-2)
print(fib(n-1))
#0 1 1 2 3 5 8 13 21
