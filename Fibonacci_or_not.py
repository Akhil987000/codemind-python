n=int(input())
a,b=0,1
c=0
for i in range(0,n+1):
    d=a+b
    a=b
    b=d
    if(d==n):
        c=c+1
if(c==1):
    print(True)
else:
    print(False)