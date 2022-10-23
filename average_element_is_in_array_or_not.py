n=int(input())
a=list(map(int,input().split()))
b=(sum(a)//len(a))
if(b in a):
    print(True)
else:
    print(False)