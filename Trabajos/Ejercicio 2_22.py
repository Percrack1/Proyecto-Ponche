a=int(input("Ingresa el primer valor entero: "))
b=int(input("Ingresa el segundo valor entero: "))
if a>b:
    temp=a
    a=b
    b=temp
print(a, "|", b)