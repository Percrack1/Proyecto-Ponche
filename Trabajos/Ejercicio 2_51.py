import numpy as np
elemento=[int() for i in range(10)]
print(elemento)
suma=0
for i in range(10):
    print("Ingresa el numero "+str(i+1)+":")
    elemento[i]=int(input())
print(elemento)
"""
for i in range(10):
    suma+=elemento[i]
print("La suma es: ", suma)
"""
suma=np.sum(elemento)
print("la suma es: ", suma)