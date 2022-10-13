n=int(input())
arr1=list(map(int,input().split()))
a=list(set(arr1))
c=[]
for i in a:
    if(arr1.count(i)==1):
        c.append(i)
if(len(c)==0):
    print("-1")
else:
    print(*c)
        