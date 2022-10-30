a,b=map(int,input().split())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
c=[]
for i in x:
    if(i in y):
        if(i in c):
            continue
        c.append(i)
print(*c)        