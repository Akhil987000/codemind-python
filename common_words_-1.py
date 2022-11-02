a=input()
b=input()
a=a.lower()
b=b.lower()
a=a.split()
b=b.split()
c=[]
for i in a:
    if(i in b):
        c.append(i)
print(len(c))