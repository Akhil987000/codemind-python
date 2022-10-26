a,b=map(int,input().split())
k=list(map(int,input().split()))
c=0
for i in k:
    if(int(i)%b==0):
        c=c+1
print(c)        