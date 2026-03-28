import numpy as np

arreglo1 = np.random.randint(100000, 1000000, 100000)
contador = 0

for num in arreglo1:
    cadena = str(num)
    mitad = len(cadena) // 2

    if len(cadena) % 2 == 0:
        parte1 = cadena[:mitad]
        parte2 = cadena[mitad:]
    else:
        parte1 = cadena[:mitad]
        parte2 = cadena[mitad+1:]

    if parte1 == parte2[::-1]:
        print(f"{cadena=} {parte1=} {parte2[::-1]=}")
        contador += 1

print("Numero total de numeros palindromos:", contador)
