num=int(input("Ingresa un numero: "))
contador=0
while num>0:
    num=num//10
    contador=contador+1
print("Numero de cifras:", contador)