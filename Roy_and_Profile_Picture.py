a=int(input())
b=int(input())
for i in range(b):
    x,y=map(int,input().split())
    if(x<a or y<a):
        print("UPLOAD ANOTHER")
    elif(x==y):
        print("ACCEPTED")
    else:
        print("CROP IT")