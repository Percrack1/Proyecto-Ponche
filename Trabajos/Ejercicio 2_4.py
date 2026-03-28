c_t=float(input("Cual es el valor total de la compra: "))
descuento=c_t*.05
s_t=c_t-descuento
iva=s_t*.16
t_p=iva+s_t
print("El monto total: $", c_t)
print("Descuento:      -", descuento)
print("    -------------")
print("subtotal:        ", s_t)
print("IVA: ", iva)
print("    -------------")
print("Totala pagar:   $", t_p)