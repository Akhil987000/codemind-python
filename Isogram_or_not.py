s=input()
z=list(s)
a=list(set(z))
c=0
for i in a:
    k=z.count(i)
    if(k==1):
        c+=1
if(c==len(z)):
    print(True)
else:
    print(False)
    