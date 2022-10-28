n=int(input())
a=list(map(int,input().split()))
c=0
d=0
for i in range(1,len(a)):
    if(i%2==0):
        c=c+a[i]
    else:
        d=d+a[i]
k=c+a[0]
b=k-d
print(b)        
        
    