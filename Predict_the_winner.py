n=int(input())
a=list(map(int,input().split()))
k=sum(a)
if(k%4==0):
    print("X")
else:
    print("Y")