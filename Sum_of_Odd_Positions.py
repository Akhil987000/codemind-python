n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(1,n):
    if(i%2!=0):
        c=c+a[i]
print(c)        
    