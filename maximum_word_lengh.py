a=input()
a=a.lower()
s=a.split()
c=[]
for i in s:
    b=len(i)
    c.append(b)
print(max(c))