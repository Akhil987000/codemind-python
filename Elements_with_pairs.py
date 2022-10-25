a=int(input())
n=list(map(int,input().split()))
if(a%2!=0):
    n.append(0)
    print(*n)
else:
    print(*n)