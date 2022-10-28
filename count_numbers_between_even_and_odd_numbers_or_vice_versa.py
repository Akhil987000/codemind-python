n=int(input())
a=list(map(int,input().split()))
c=0
d=0
e=0
f=0
for i in range(len(a)-2):
    if(a[i]%2==0 and a[i+1]%2==0 and a[i+2]%2!=0):
        c=c+1
    elif(a[i]%2!=0 and a[i+1]%2==0 and a[i+2]%2==0):
        d=d+1
    elif(a[i]%2==0 and a[i+1]%2!=0 and a[i+2]%2!=0):
        e=e+1
    elif(a[i]%2!=0 and a[i+1]%2!=0 and a[i+2]%2==0):
        f=f+1
print(c+d+e+f)    