n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
    j=str(i)
    k=j[::-1]
    if(j==k):
        c=c+1
print(c)