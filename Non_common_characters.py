a=input()
b=input()
a=a.lower()
b=b.lower()
a=a.split()
b=b.split()
a=''.join(a)
b=''.join(b)
a=list(a)
b=list(b)
z=set(a).symmetric_difference(set(b))
z=list(z)
z.sort()
z=''.join(z)
print(len(z))