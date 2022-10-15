s=input()
a=0
b=0
c=0
d=0
for i in s:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        a+=1
    elif(i in "0123456789"):
        c+=1
    elif(i==' '):
        d+=1
    else:
        b+=1
print("Vowels:",a)
print("Consonants:",b)
print("Digits:",c)
print("White spaces:",d)        