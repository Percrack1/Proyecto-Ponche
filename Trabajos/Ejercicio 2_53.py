arreglo=[]
print(arreglo)
for i in range(20):
    i+=1
    caracter=str(input("Cadena "+str(i)+": "))
    arreglo.append(caracter)
print(" Desordenado ")
print(arreglo)
print(" Ascendente ")
arreglo.sort()
print(arreglo)
print(" Descendente ")
arreglo.sort(reverse=True)
print(arreglo)