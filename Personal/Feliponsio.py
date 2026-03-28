import tkinter as tk
from PIL import Image, ImageTk

def mostrar_imagen(ruta):
    ventana = tk.Tk()
    ventana.title("Resultado")

    img = Image.open(ruta)
    img = img.resize((300, 300))
    img_tk = ImageTk.PhotoImage(img)

    label = tk.Label(ventana, image=img_tk)
    label.image = img_tk
    label.pack()

    ventana.mainloop()


a = input("¿Feliponsio es puto? (si/no): ").lower()

if a == "si":
    print("Felicidades acertaste :D")

elif a == "no":
    a = input(
        "Parece ser que te equivocaste al responder, creo que quisiste decir que -si- no? (si/no): "
    ).lower()

    if a == "no":
        a = input("¿Completamente seguro? (si/no): ").lower()

        if a == "si":
            print("Pinche puto te equivocaste, el Feliponsio sí es puto D:<")
            mostrar_imagen(r"C:\Users\rupan\Documents\VSC\Python\Img\OIP.jpg")

        elif a == "no":
            print("Que bueno que al final recapacitaste :D")

    elif a == "si":
        print("Que bien, por un momento pensé que también eras puto :D")

else:
    print("Responde solo con 'si' o 'no' cabron")