n=3
for i in range(0,n):
    for j in range(0,n):
        if i==j or i+j==n-1:
            print('*',end='')
        else:
            print(' ',end='')
    print('')
n=5
for i in range(0,n):
    for j in range(0,n):
            print('*',end='')
    print('')    
