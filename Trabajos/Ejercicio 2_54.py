import random
import math

n = int(input("Ingrese el tamaño del arreglo: "))

arreglo = []
suma = 0

for i in range(n):
    num = random.randint(1, 100)
    arreglo.append(num)
    suma += num

media = suma / n

suma2 = 0
for i in range(n):
    suma2 += (arreglo[i] - media) ** 2

desviacion = math.sqrt(suma2 / n)

print("Arreglo:", arreglo)
print("Media:", media)
print("Desviación estándar:", desviacion)