import random

n = int(input("Ingrese el tamaño de los arreglos: "))

arreglo1 = []
arreglo2 = []

for i in range(n):
    arreglo1.append(random.randint(1, 100))
    arreglo2.append(random.randint(1, 100))

suma = []
resta = []
multiplicacion = []
division = []

for i in range(n):
    suma.append(arreglo1[i] + arreglo2[i])
    resta.append(arreglo1[i] - arreglo2[i])
    multiplicacion.append(arreglo1[i] * arreglo2[i])

    if arreglo2[i] != 0:
        division.append(arreglo1[i] / arreglo2[i])
    else:
        division.append(0)

print("Arreglo 1:", arreglo1)
print("Arreglo 2:", arreglo2)
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)