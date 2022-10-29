n=int(input())
a=list(map(int,input().split()))
k=list(set(a))
d=0
for i in range(len(k)):
    if(a.count(k[i])==k[i]):
        d=d+1
print(d)