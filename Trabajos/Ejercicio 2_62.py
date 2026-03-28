fila_a_num = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12, "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26}

luneta = [[0 for i in range(35)] for j in range(27)]
balcon1 = [[0 for i in range(32)] for j in range(10)]
balcon2 = [[0 for i in range(30)] for j in range(8)]

def convertir_fila(fila):
    fila = fila.upper()
    if fila in fila_a_num:
        return fila_a_num[fila]
    return -1


while True:
    print("\n---- Venta de boletos ----")
    print("1 - Luneta")
    print("2 - 1er Balcón")
    print("3 - 2° Balcón")
    print("4 - Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "4":
        print("Gracias por usar el sistema.")
        break

    if opcion not in ["1", "2", "3"]:
        print("Opción inválida.")
        continue

    fila = input("Ingrese la fila (letra): ").upper()
    f = convertir_fila(fila)

    if f == -1:
        print("Esta fila no existe.")
        continue

    try:
        butaca = int(input("Ingrese número de butaca: "))
    except:
        print("Número inválido.")
        continue

    if opcion == "1":
        if f < 1 or f > 27 or butaca < 1 or butaca > 35:
            print("Butaca fuera de rango.")
            continue

        if luneta[f - 1][butaca - 1] == 0:
            luneta[f - 1][butaca - 1] = 1
            print(f"BUTACA VENDIDA: Luneta Fila {fila} Butaca {butaca}")
        else:
            print("Esa butaca ya está ocupada.")

    elif opcion == "2":
        if f < 1 or f > 10 or butaca < 1 or butaca > 32:
            print("Butaca fuera de rango.")
            continue

        if balcon1[f - 1][butaca - 1] == 0:
            balcon1[f - 1][butaca - 1] = 1
            print(f"BUTACA VENDIDA: 1er Balcón Fila {fila} Butaca {butaca}")
        else:
            print("Esa butaca ya está ocupada.")

    elif opcion == "3":
        if f < 1 or f > 8 or butaca < 1 or butaca > 30:
            print("Butaca fuera de rango.")
            continue

        if balcon2[f - 1][butaca - 1] == 0:
            balcon2[f - 1][butaca - 1] = 1
            print(f"BUTACA VENDIDA: 2º Balcón Fila {fila} Butaca {butaca}")
        else:
            print("Esa butaca ya está ocupada.")