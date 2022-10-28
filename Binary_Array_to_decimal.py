n=int(input())
a=list(map(int,input().split()))
c=''
for i in a:
    c=c+str(i)
c=int(c,2)
print(c)