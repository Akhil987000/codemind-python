n=int(input())
a=list(map(int,input().split()))
for i in a:
    j=str(i)
    k=j[::-1]
    print(int(k),end=' ')