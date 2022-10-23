a=int(input())
b=list(map(int,input().split()))
x,y=map(int,input().split())
c=0
for i in range(0,len(b)):
    if(b[i] in range(x,y+1)):
        continue
    else:
        c=c+b[i]
print(c)        
    