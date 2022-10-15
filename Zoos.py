s=input()
x=0
y=0
a=list(s)
for i in a:
    if(i=='z'):
        x+=1
    elif(i=='o'):
        y+=1
if(2*x==y):
    print("Yes")
else:
    print("No")
    