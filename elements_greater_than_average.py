n=int(input())
a=list(map(int,input().split()))
b=(sum(a)//len(a))
c=[]
for i in a:
    if(i>=b):
        c.append(i)
print(len(c))        