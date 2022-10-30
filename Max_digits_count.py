a=int(input())
x=list(map(int,input().split()))
c=[]
for i in x:
    if(i<0):
        i=i*-1
    z=list(str(i))
    k=len(z)
    c.append(k)
    r=max(c)
print(c.count(r))