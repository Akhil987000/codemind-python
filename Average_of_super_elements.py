n=int(input())
a=list(map(int,input().split()))
h=list(set(a))
c=[]
for i in h:
    if(a.count(i)==i):
        c.append(i)
if(len(c)==0):
    print(-1)
else:
    s=sum(c)/len(c)
    print("%.2f"%s)