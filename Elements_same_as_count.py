n=int(input())
a=list(map(int,input().split()))
c=[]
d=0
for i in a:
    if(a.count(i)==i):
        if(i not in c):
            d+=1
            c.append(i)
if(d==0):
    print(-1)
else:
   print(*c)