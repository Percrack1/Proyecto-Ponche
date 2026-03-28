mes=int(input("Ingresa el mes: "))
dia=int(input("Ingresa el dia: "))
if mes>=1 and mes<=12:
    if dia>=1 and dia<=31:
        print("Fecha correcta")
    else:
        print("Fecha incorrecta")
else:
    print("Fecha incorrecta")