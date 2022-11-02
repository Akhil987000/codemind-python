s=input()
s=s.lower()
a=list(s)
k=list(set(a))
c=0
for i in k:
    if(i==" "):
        c+=1
print(len(k)-c)