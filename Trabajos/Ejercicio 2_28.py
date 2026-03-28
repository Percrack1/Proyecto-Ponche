mc=input("Ingresa su tipo de membresía (A, B o C): ")
ct=float(input("Ingresa el costo total: "))
if mc=="A":
    temp=ct*.10
    tp=ct-temp
    print("El total a pagar es de:", tp)
else:
    if mc=="B":
        temp=ct*.15
        tp=ct-temp
        print("El total a pagar es de:", tp)
    else:
        if mc=="C":
            temp=ct*.20
            tp=ct-temp
            print("El total a pagar es de:", tp)