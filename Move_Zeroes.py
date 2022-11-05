n=int(input())
a=list(map(int,input().split()))
c=a.count(0)
d=[]
for i in a:
    if(i!=0):
        d.append(i)
for j in range(c):
    d.append(0)
print(*d)
    