n=int(input())
a=list(map(int,input().split()))
l=int(input())
def primes(n):
    if(n<=1):
        return False
    for i in range(2,n):
        if(n%i==0):
            return False
    return True
c=[]
for j in a:
    if(primes(j) and j>=l):
        c.append(j)
print(len(c))        
