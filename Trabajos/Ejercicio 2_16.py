nombre=input("Ingresa el nombre: ")
horas=float(input("Ingresa las horas trabajadas: "))
precio=float(input("Ingresa el pago por hora: "))
salariobruto=horas*precio
impuesto=salariobruto*0.20
salarioneto=salariobruto-impuesto
print("Nombre:", nombre)
print("Salario bruto:", salariobruto)
print("Impuesto:", impuesto)
print("Salario neto:", salarioneto)