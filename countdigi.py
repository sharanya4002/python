s='1234$AB'
count=0
for i in s:
    if (not(i.isdigit())):
        count+=1
print(count)
