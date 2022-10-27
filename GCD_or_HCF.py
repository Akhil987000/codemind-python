a,b=map(int,input().split())
if(a>b):
    min1=b
else:
    min1=a
for i in range(1,min1+1):    
    if(a%i==0 and b%i==0):
        hcf=i
print(hcf)