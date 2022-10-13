n=int(input())
arr1=list(map(int,input().split()))
a=list(set(arr1))
c=[]
for i in a:
    b=arr1.count(i)
    c.append(b//2)
print(sum(c))        
            
    