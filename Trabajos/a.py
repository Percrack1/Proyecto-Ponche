frutas=["Manzana", "Banana", "Cereza"]
for fruta in frutas:
    print(fruta, len(fruta), end="")
    contador=0
    for letra in fruta:
        if letra.lower() in "aáeéiíoóuú":
            contador+=1
    print("", contador)