a=float(input("Da el primer valor: "))
b=float(input("Da el segundo valor: "))
c=float(input("Da el tercer valor: "))
d=float(input("Da el cuarto valor: "))
if a<b:
    temp=a
    a=b
    b=temp
if a<c:
    temp=a
    a=c
    c=temp
if a<d:
    temp=a
    a=d
    d=temp
if b<c:
    temp=b
    b=c
    c=temp
if b<d:
    temp=b
    b=d
    d=temp
if c<d:
    temp=c
    c=d
    d=temp
print(a, "|", b, "|", c, "|", d)