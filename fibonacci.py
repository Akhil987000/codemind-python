n=int(input())
a,b=0,1
c=0
if(n<=0):
    print(0)
elif(n==1):
    print(n)
else:
    while(c<n):
        print(a,end=' ')
        d=a+b
        a=b
        b=d
        c+=1
