calificaciones = []

for i in range(10):
    cal = int(input(f"Ingrese la calificación {i}: "))
    calificaciones.append(cal)

print("Índices de calificaciones aprobatorias (>=70):")

for i in range(10):
    if calificaciones[i] >= 70:
        print(i)