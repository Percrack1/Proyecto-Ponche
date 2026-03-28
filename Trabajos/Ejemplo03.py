import time
import numpy as np

mi_lista=[10, 15, 25, 50, 21]
print("mi_lista", mi_lista)
print("mi_lista", mi_lista[0])
print("mi_lista[-1]=", mi_lista[-1])
print("mi_lista[2:4]=", mi_lista[2:4])
print("mi_lista[:4]=", mi_lista[:4])
print("mi_lista[2:]=", mi_lista[2:])
x=mi_lista.copy()
x.append(100)
print("mi_lista", mi_lista)