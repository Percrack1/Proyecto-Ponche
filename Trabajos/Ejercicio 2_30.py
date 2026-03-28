a=float(input("Da el primer valor: "))
b=float(input("Da el segundo valor: "))
c=float(input("Da el tercer valor: "))
if a>b and a>c:
    print(a, "es el numeo mayor")
else:
    if b>a and b>c:
        print(b, "es el numero mayor")
    else:
        print(c, "es el numero mayor")