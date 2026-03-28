suma=0
contador=0
num=float(input("Ingresa un numero positivo (negativo para terminar): "))

while num>=0:
    suma+=num
    contador=contador+1
    num=float(input())

media=suma/contador
print("La media es:", media)
