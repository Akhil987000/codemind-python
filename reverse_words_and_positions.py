a=input()
a=a.lower()
s=a.split()
d=s[::-1]
for i in d:
    print(i[::-1],end=' ')