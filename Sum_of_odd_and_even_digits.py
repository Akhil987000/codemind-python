n=int(input())
a=list(map(int,input().split()))
x,y=0,0
for i in range(len(a)):
    if(i%2==0):
        x=x+a[i]
    else:
        y=y+a[i]
if(x-y==0):
    print("YES")
else:
    print("NO")