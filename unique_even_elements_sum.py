a=int(input())
n=list(map(int,input().split()))
b=set(n)
c=[]
for i in b:
    if(i%2==0):
        c.append(i)
print(sum(c))        