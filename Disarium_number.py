n=int(input())
a=list(str(n))
b=0
for i in range(len(a)):
    b+=int(a[i])**(i+1)
if(b==n):
    print(True)
else:
    print(False)