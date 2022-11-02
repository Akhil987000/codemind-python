s=input()
c=[]
for i in s:
    if(s.count(i)==1):
        c.append(i)
if(len(c)==0):
    print(-1)
else:
    print(c[0])    