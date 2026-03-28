nombre=input("Ingrese su Nombre: ")
for i in range(len(nombre),0,-1):
    print(nombre[i-1:])
for i in range(len(nombre)):
    print(nombre[i:len(nombre)-i])
for i in range(1,len(nombre)+1):
    print(nombre[:i])
