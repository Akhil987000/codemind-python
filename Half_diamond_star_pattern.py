n=int(input())
if(n>=3):
    for i in range(1,n+1):
        print(i*"*")
    c=n
    for j in range(1,n):
        c=n-j
        print(c*"*")
else:
    print("The pattern is not possible")