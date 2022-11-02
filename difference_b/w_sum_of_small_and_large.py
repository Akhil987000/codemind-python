a=input()
s=a.split()
c=[]
d=[]
for i in s:
    c.append(ord(min(i)))
    d.append(ord(max(i)))
    x=sum(c)
    y=sum(d)
print(y-x)
    