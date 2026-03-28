import numpy as np
arreglo1=np.random.randint(0, 10, 10)
arreglo2=np.random.randint(0, 10, 10)
print(arreglo1)
print(arreglo2)
mult=np.multiply(arreglo1, arreglo2)
print(mult)
print("El numero mas grande de la lista es: ", np.max(mult))