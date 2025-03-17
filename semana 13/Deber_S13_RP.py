import tkinter as tk

#Creo la ventana
def agregar():
    dato =entrada.get().strip()
    if dato:
        lista.insert(tk.END, dato)

def limpiar():
    lista.delete(0, tk.END)
    entrada.delete(0, tk.END)
root = tk.Tk()
#se crea nombre
root.title ("Semana 13")
#Se crea un tamaño
root.geometry("700x400")
#Escojo el color de fondo :D
root.configure(bg="sky blue")
#Se crea el label

#Se crea la entrada
entrada = tk.Entry(root, bg="orange")
entrada.pack(pady = 10)
#se agrega el botón
boton = tk.Button(root, text="Agregar", background="gray", font="Cambria", command=agregar)
boton.pack( pady = 20)

#Se crea la lista
lista = tk.Listbox(root)
lista.pack(pady = 30)

boton_limpiar = tk.Button(root, text="Limpiar texto", background="gray", font="Cambria", command=limpiar)
boton_limpiar.pack( pady = 5)

#aquí inicia la ventana

root.mainloop()


