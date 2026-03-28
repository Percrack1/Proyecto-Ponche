MAX = 20

n = int(input("Ingrese el número de alumnos (máximo 20): "))

nombres = []
calif = [[0]*4 for _ in range(MAX+1)]

for i in range(n):
    nombre = input(f"Nombre del alumno {i+1}: ")
    nombres.append(nombre)

    calif[i][0] = int(input("Calificación Materia 1: "))
    calif[i][1] = int(input("Calificación Materia 2: "))
    calif[i][2] = int(input("Calificación Materia 3: "))

    calif[i][3] = (calif[i][0] + calif[i][1] + calif[i][2]) / 3

for m in range(3):
    suma = 0
    for i in range(n):
        suma += calif[i][m]
    calif[20][m] = suma / n

sumaG = 0
for i in range(n):
    sumaG += calif[i][3]
calif[20][3] = sumaG / n

print("\nNo.  Nombre           M1   M2   M3   Prom")
for i in range(n):
    print(f"{i+1:<4} {nombres[i]:<15} {calif[i][0]:<4} {calif[i][1]:<4} {calif[i][2]:<4} {calif[i][3]:.2f}")

print("\nPromedios:", end=" ")
for j in range(4):
    print(f"{calif[20][j]:.2f}", end=" ")
print()