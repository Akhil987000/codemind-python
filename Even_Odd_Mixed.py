a=int(input())
n=list(str(a))
c=0
d=0
for i in n:
    if(int(i)%2==0):
        c=c+1
    elif(int(i)%2!=0):
        d=d+1
if(c==len(n)):
    print("Even")
elif(d==len(n)):
    print("Odd")
else:
    print("Mixed")
        
    