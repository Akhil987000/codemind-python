n=int(input())
m=str(n)
k=m[::-1]
l=int(k)
c=0
d=0
for i in range(2,n+1):
    if(n%i==0):
        c+=1
for j in range(2,l+1):
    if(l%j==0):
        d=d+1
if(c==1 and d==1):
    print("circular prime")
elif(c==1 and d!=1):
    print("prime but not a circular prime")
elif(c!=1 and d!=1):
    print("not prime")