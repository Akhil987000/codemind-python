s=input()
c=[]
for i in s:
    if(i in "0123456789"):
        c.append(int(i))
print(sum(c))        