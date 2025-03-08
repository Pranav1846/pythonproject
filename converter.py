n="hellow 123."
out=''
for i in n:
    if i.isupper():
        o=i.lower()
    elif i.lower():
        o=i.upper()
    else:
        o=i
    out+=o
print(out)    
    
