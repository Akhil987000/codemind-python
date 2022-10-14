n=int(input())
arr1=list(map(int,input().split()))
c=0
for i in arr1:
    b=len(str(i))
    if(b%2==0):
        c+=1
print(c)