n=int(input())
z=str(n)
c=0
d=1
for i in z:
    c+=int(i)
    d=d*int(i)
if(c==d):
    print("Spy Number")
else:
    print("Not Spy Number")
