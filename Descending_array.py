n=int(input())
a=list(map(int,input().split()))
b=sorted(a)
c=b[::-1]
if(a==c and len(a)==len(set(a))):
    print("yes")
else:
    print("no")