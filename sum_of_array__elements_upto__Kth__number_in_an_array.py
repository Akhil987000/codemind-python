a=int(input())
n=list(map(int,input().split()))
k=int(input())
c=0
for i in n:
    c=c+i
    if(i==k):
        
        break
print(c)    
        