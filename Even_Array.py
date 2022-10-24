n=int(input())
a=list(map(int,input().split()))
c=[]
for i in a:
    if(i%2==0):
        c.append(i)
if(a==c):
    print(True)
else:
    print(False)