a=input()
k=list(a)
c=0
for i in k:
    if(i in "0123456789"):
        c=c+int(i)
print(c)
    