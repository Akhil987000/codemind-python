a=int(input())
def sq(a):
    k=0
    while(a):
        c=a%10
        k=k+c**2
        a=a//10
    return k
while(a):
    if(a<10):
        if(a==1 or a==7):
            print(True)
            break
        else:
            print(False)
            break
    else:
        a=sq(a)
    