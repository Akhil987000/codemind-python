n=int(input())
y=len(str(n))
a=n*n
z=a%pow(10,y)
if(n==z):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")