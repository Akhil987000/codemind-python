n=int(input())
a=n*n
b=len(str(n))
k=list(str(a))
h=len(k)-b
r=k[h:]
r="".join(r)
r=int(r)
if(r==n):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")
