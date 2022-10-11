import math
a,b=map(int,input().split())
if(a>b):
    g=a
else:
    g=b
while(True):
    if(g%a==0 and g%b==0):
        lcm=g
        print(lcm)
        break
    g+=1
    
        