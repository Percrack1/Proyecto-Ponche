# Lista de NO. de trabajadores
a=[100, 110, 130 , 135, 143, 150, 163, 174, 183, 192, 203, 213, 226, 234, 241, 255, 261, 274, 283, 294, 307, 318, 326, 331, 337]

# Lista de nombres
b=["Jose Perez Ramos", "Pablo Ramirez Ruiz", "Ma. Luz Aguilar Hernandez", "Roberto Haro Torres", "Rosa Lopez Juarez", "Ramon Martinez Suarez",
 "Santiago Alonso Contreras", "Jesus Campos Sanchez", "Moises Castro Montante", "Pablo Cervantes Salinas", "Anahi Torres Carreon",
 "Nuria Lira Gonzalez", "Miguel Mendoza Sanchez", "Sofia Gonzalez Esparza", "Cristian Gonzalez Gonzalez ", "Juan Gamez Aguilar",
 "Fernando Lopez Nuño"," Abraham Lozano De Lira", "Angel Negrete Demetrio", "Damian Nieves Quesada", "Armando Reyez Martinez",
 "Manuel Ruiz Mendoza", "Esteban Salado Muñoz", "Alejandro Soto Ocampo", "Alondra Valdez Mora"]

# Lista de departamentos
c=["Producción", "Producción", "Producción", "Ventas", "Ventas", "Ventas", "Compras", "Compras", "Compras", "Recursos Humanos",
 "Recursos Humanos", "Recursos Humanos", "Produccion", "Dirección ", "Produccion", "Ventas", "Dierección", "Compras", "Ventas",
 "Recursos Humanos", "Compras", "Ventas", "Dirección", "Dirección", "Dirección"]

# Lista de tipos de empleado
d=["Obrero", "Obrero", "Obrero", "Empleado", "Empleado", "Empleado", "Empleado", "Empleado", "Empleado", "Empleado", "Empleado", "Empleado",
 "Empleado","Directivo", "Obrero", "Empleado", "Empleado", "Empleado", "Empleado", "Empleado", "Empleado", "Empleado","Directivo",
 "Directivo", "Directivo",]

# Lista de días trabajados
e=[7, 7, 7, 15, 15, 15, 15, 15, 15, 15, 15, 15,7,15, 7, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15,]

# Lista del pago diario
f=[825,825,825,955,955,955,955,955,955,955,955,955,825, 2000, 825, 955, 1200, 955, 955, 955, 955, 955, 1500, 1200, 1200]

# Lista de horas extra trabajadas
g=[9,10,12,10,4,9,11,11,0,6,3,0,1,0,6,8,1,8,1,10,8,3,0,0,0]

# Lista de pago por horas extra
h=[200,200,200,250,250,250,250,250,250,250,250,250,200,0,200,250,250,250,250,250,250,250,0,0,0]

# Lista de bonos adicionales
i=[0,0,0,0,0,0,0,0,0,0,0,0,0,800,0,0,0,0,0,0,0,0,1000,1200,2000]

# Crear matriz vacía de 25 filas y 9 columnas
matriz=[[0]*9 for i in range(25)]

# Llena la matriz con la información de cada empleado
for fil in range(25):
    matriz[fil][0]=a[fil]  # ID
    matriz[fil][1]=b[fil]  # Nombre
    matriz[fil][2]=c[fil]  # Departamento
    matriz[fil][3]=d[fil]  # Puesto
    matriz[fil][4]=e[fil]  # Días trabajados
    matriz[fil][5]=f[fil]  # Pago diario
    matriz[fil][6]=g[fil]  # Horas extra
    matriz[fil][7]=h[fil]  # Pago horas extra
    matriz[fil][8]=i[fil]  # Bonos

# Función que muestra el menú del sistema
def menu():
    print("========================================")
    print("      SISTEMA DE GESTIÓN DE SUELDOS")
    print("========================================\n")
    
    # Opciones del menú
    print("  1. Modificar información")
    print("  2. Calcular sueldos")
    print("  3. Desplegar sueldos")
    print("  4. Sueldos por departamentos")
    print("  5. Sueldos por tipo de empleado")
    print("  6. Sueldos, horas extra y bonos")
    print("  7. Salir\n")
    
    print("========================================")
    
    # Solicita al usuario seleccionar una opción
    op=input("Seleccione una opción: ")

# Llamada a la función menú
menu()