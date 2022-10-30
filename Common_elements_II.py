a,b=map(int,input().split())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
c=[]
for i in x:
    if(i not in y):
        c.append(i)
for j in y:
    if(j not in x):
        c.append(j)
print(*c)        