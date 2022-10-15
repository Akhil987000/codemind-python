t=int(input())
for i in range(t):
    s=input()
    a=s[::-1]
    d=len(s)
    if(s!=a):
        print("NO")
    elif(s==a and d%2==0):
        print("YES EVEN")
    elif(s==a and d%2!=0):
        print("YES ODD")