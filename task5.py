def valid_str(s):
    u=False
    l=False
    d=False
    sc=False
    for char in s:
        if 'A'<= char<='Z':
            u=True
        elif 'a'<=char<='z':
            l=True
        elif '0' <= char <='9':
            d=True
        elif char in '!@#$%^&*':
            sc=True
        
    if  len(s)>8 and u and l and d and sc:
        return 'valid'
    else:
        return 'Invalid'
s=input()
print(valid_str(s))
