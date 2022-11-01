a=input()
s=a.split()
def vowel(a):
    c=0
    for i in a:
        if(i in "aeiou"):
            c+=1
    return c
d=[]
for j in s:
    a=vowel(j)
    d.append(a)
print(max(d))
   
            