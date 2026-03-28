compra=float(input("Ingresa el costo total: "))
if compra>15000:
    temp=compra*.10
    cf=compra-temp
else:
    temp=compra*.5
    cf=compra-temp

print("El total a pagar despues del descuento es de:", cf)