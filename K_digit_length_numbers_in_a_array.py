a,b=map(int,input().split())
x=list(map(int,input().split()))
c=0
for i in range(0,len(x)):
    if(x[i]<0):
        x[i]=x[i]*-1
    z=list(str(x[i]))
    if(len(z)==b):
        c=c+1
print(c)