s=input()
s=s.lower()
s=s.split()
j=''.join(s)
a=list(j)
k=list(set(a))
c=[]
for i in k:
    if(a.count(i)==1):
        c.append(i)
        m=sorted(c)
        z=''.join(m)
print(len(z))
