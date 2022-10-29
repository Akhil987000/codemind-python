n=int(input())
a=list(map(int,input().split()))
c=0
d=0
for i in range(1,(len(a)//2)+1):
    c=c+i
for j in range(i+1,(len(a)+1)):
    d=d+j
if(c>=d):
    print(c-d)
else:
    print(d-c)
