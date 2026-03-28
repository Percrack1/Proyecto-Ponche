c1=float(input("Ingresa la primera calificacion: "))
c2=float(input("Ingresa la segunda calificacion: "))
c3=float(input("Ingresa la tercera calificacion: "))
ct=(c1+c2+c3)/3
if ct>=70:
    print("Aprobaste")
else:
    print("Reprobaste")