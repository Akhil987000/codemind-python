for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    d=(n*(n+1))//2
    print(d-sum(a))