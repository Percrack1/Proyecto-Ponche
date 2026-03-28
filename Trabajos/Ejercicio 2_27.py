zc=int(input("Ingresa la cantidad de pares de zapatos: "))
ct=int(input("Ingresa el costo de los zapatos: "))
if zc>10 and zc<=20:
    cf=zc*ct
    temp=cf*.10
    cf=cf-temp
    print("El costo total es de:", cf)
else:
    if zc>20 and zc<=30:
        cf=zc*ct
        temp=cf*.20
        cf=cf-temp
        print("El costo total es de:", cf)
    else:
        if zc>30:
            cf=zc*ct
            temp=cf*.30
            cf=cf-temp
            print("El costo total es de:", cf)
        else:
            cf=zc*ct
            print("El costo total es de:", cf)
