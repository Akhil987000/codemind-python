n=int(input())
arr1=list(map(int,input().split()))
c=[]
for i in arr1:
    a=i*i
    c.append(a)
print(*sorted(c))    
    