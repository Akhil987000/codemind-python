n=int(input())
a=list(map(int,input().split()))
x,y=map(int,input().split())
c=[]
for i in range(len(a)):
    if(a[i]<x or a[i]>y):
        c.append(a[i])
if(len(c)==0):
    print(-1)
else:    
    print(max(c))        