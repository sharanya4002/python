s=input()
res= int(s[0])
for c in range(1,len(s),2):
    if s[c]=='a':
        res=res&int(s[c+1])
    if s[c] =='b':
        res = res|int(s[c+1])
    if s[c] =='c':
        res = res ^int(s[c+1])
print(res)
