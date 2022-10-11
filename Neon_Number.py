n=int(input())
a=n*n
b=str(a)
c=0
for i in b:
    c+=int(i)
if(n==c):
    print("Neon Number")
else:
    print("Not Neon Number")