mayor=0
num=int(input("Ingresa numeros (0 para terminar): "))

while num!=0:
    if num>mayor:
        mayor=num
    num=int(input())

print("El numero mayor es:", mayor)