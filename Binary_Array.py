a=int(input())
n=list(map(int,input().split()))
c=0
for i in n:
    if(i==0 or i==1):
        continue
    else:
        c=c+1
        break
if(c>0):
    print(False)
else:
    print(True)