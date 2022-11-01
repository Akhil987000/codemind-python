n=int(input())
a=list(map(int,input().split()))
def avg_pri(n):
    if(n<=1):
        return False
    for i in range(2,n):
        if(n%i==0):
            return False
    return True
c=[]
for i in a:
    if(avg_pri(i)):
        c.append(i)
d=(sum(c)/len(c))
print("%.2f"%d)
