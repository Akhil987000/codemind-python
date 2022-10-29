n=int(input())
a=list(map(int,input().split()))
h=list(set(a))
r=[]
q=[]
for i in a:
    y=a.count(i)
    if(i not in q):
        q.append(i)
        r.append(i)
        r.append(y)
print(*r)
    
    