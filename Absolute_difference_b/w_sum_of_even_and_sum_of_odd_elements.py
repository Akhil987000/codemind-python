n=int(input())
a=list(map(int,input().split()))
c=0
d=0
for i in a:
    if(i%2==0):
        c=c+i
    else:
        d=d+i
if(c>=d):
    print(c-d)
else:    
    print(d-c)        