n=int(input())
a=list(map(int,input().split()))
b=sorted(a)
if(a==b and len(a)==len(set(a))):
    print("yes")
else:
    print("no")