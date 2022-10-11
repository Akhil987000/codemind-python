n=int(input())
c=0
for i in range(n):
    for j in range(i+1,n+1):
        if(i*i+j*j==n):
            c=1

if(c==1):
    print(True)
else:
    print(False)