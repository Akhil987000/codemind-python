a=input()
s=a.split()
c=[]
d=[]
for i in s:
    c.append(ord(min(i)))
    d.append(ord(max(i)))
for j in range(len(c)):
    print((d[j]-c[j]),end=' ')