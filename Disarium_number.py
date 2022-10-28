n=int(input())
s=list(map(int,str(n)))
c=0
for i in range(0,len(s)):
    a=((s[i])**(i+1))
    c=c+a
if(c==n):
    print(True)
else:
    print(False)