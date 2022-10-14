n=int(input())
arr1=list(map(int,input().split()))
a=list(set(arr1))
c=[]
for i in a:
    if((arr1.count(i))>(n//2)):
        c.append(i)
print(*c)


        
    
    