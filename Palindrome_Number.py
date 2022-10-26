z=int(input())
for i in range(z):
    n=int(input())
    b=str(n)
    c=b[::-1]
    if(int(c)==n):
        print(True)
    else:
        print(False)