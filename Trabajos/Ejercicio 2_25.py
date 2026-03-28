hr=float(input("Ingresa tus horas trabajadas: "))
if hr>40:
    temp=hr-40
    extra=temp*25
    pago=40*20+extra
    print("Tu paga es de:", pago)
else:
    pago=hr*20
    print("Tu paga es de:", pago)