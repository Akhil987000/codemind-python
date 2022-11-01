a=input()
s=a.split()
d=0
s=list(map(str,s))
for i in s:
    if(i[0] in "aeiouAEIOU" and i[-1] not in "aeiouAEIOU"):
        d+=1
print(d)        
        
        