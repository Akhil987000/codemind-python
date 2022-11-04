n=int(input())
c=[]
for i in range(1,n):
    if(n%i==0):
        c.append(i)
if(n==sum(c)):
    print(True)
else:
    print(False)