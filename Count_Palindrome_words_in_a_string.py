a=input()
a=a.lower()
s=a.split()
z=0
for i in s:
    b=list(i)
    c=b[::-1]
    if(b==c):
        z=z+1
print(z)