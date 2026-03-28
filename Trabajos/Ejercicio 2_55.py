import random

n = int(input("Ingrese el tamaño del arreglo: "))

arreglo = []

for i in range(n):
    arreglo.append(random.randint(1, 100))

maximo = arreglo[0]
minimo = arreglo[0]

for i in range(1, n):
    if arreglo[i] > maximo:
        maximo = arreglo[i]
    if arreglo[i] < minimo:
        minimo = arreglo[i]

print("Arreglo:", arreglo)
print("Valor máximo:", maximo)
print("Valor mínimo:", minimo)