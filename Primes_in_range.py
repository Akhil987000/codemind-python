import math
m=int(input())
n=int(input())
c=0
def primes_ran(a):
    if a<=1:
        return 0
    for i in range(2,(int(math.sqrt(a)))+1):
        if(a%i==0):
            return 0
    return 1
for j in range(m,n+1):
    if(primes_ran(j)):
        c+=1
print(c)        
        