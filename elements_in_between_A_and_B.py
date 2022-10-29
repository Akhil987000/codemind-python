n=int(input())
a1=list(map(int,input().split()))
a,b=map(int,input().split())
c=[]
for i in a1:
    if(int(i)>=a and int(i)<=b):
        c.append(i)
if(len(c)==0):
    print(-1)
else:
    print(*c)
        