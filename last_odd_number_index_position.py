a=int(input())
z=list(map(int,input().split()))
for i in range(0,len(z)):
    if(z[i]%2!=0):
        y=i
print(y)        