a=raw_input()
n=len(a)
b=''
for  y in range(-1,-(n+1),-1):
   
    if a[y]!='a' and a[y]!='e' and a[y]!='i' and a[y]!='o' and a[y]!='u':
        z=a[y]
        b=b+z
print(b)
