s=input()
l=input()
a=list(s)
c=0
for i in a:
    if(i==l):
        k=a.index(i)
        c+=1
if(c==0):
    print(False)
else:
    print(True)
    print(k)
    