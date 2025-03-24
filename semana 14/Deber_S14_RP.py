import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry


# Función para agregar un evento
def agregar_evento():
    fecha = entry_fecha.get()
    hora = entry_hora.get().strip()
    descripcion = entry_descripcion.get().strip()

    if fecha and hora and descripcion:
        tree.insert("", tk.END, values=(fecha, hora, descripcion))
        entry_hora.delete(0, tk.END)
        entry_descripcion.delete(0, tk.END)
    else:
        messagebox.showwarning("Entrada inválida", "Todos los campos deben estar llenos.")


# Función para eliminar un evento seleccionado
def eliminar_evento():
    seleccionado = tree.selection()
    if seleccionado:
        tree.delete(seleccionado)
    else:
        messagebox.showwarning("Eliminar", "Por favor, selecciona un evento para eliminar.")


# Crear ventana principal
root = tk.Tk()
root.title("Gestor de Eventos")
root.geometry("600x400")
root.configure(bg="lightblue")

# Frame para la entrada de datos
frame_entrada = tk.Frame(root, bg="lightblue")
frame_entrada.pack(pady=10)

# Etiquetas y entradas para fecha, hora y descripción
tk.Label(frame_entrada, text="Fecha:", bg="lightblue").grid(row=0, column=0, padx=5, pady=5)
entry_fecha = DateEntry(frame_entrada, width=12, background='darkblue', foreground='white', borderwidth=2)
entry_fecha.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_entrada, text="Hora:", bg="lightblue").grid(row=1, column=0, padx=5, pady=5)
entry_hora = tk.Entry(frame_entrada)
entry_hora.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_entrada, text="Descripción:", bg="lightblue").grid(row=2, column=0, padx=5, pady=5)
entry_descripcion = tk.Entry(frame_entrada, width=40)
entry_descripcion.grid(row=2, column=1, padx=5, pady=5)

# Botones para agregar y eliminar eventos
btn_agregar = tk.Button(root, text="Agregar Evento", command=agregar_evento)
btn_agregar.pack(pady=5)
btn_eliminar = tk.Button(root, text="Eliminar Evento Seleccionado", command=eliminar_evento)
btn_eliminar.pack(pady=5)

# TreeView para mostrar los eventos
tree = ttk.Treeview(root, columns=("Fecha", "Hora", "Descripción"), show="headings")
tree.heading("Fecha", text="Fecha")
tree.heading("Hora", text="Hora")
tree.heading("Descripción", text="Descripción")
tree.pack(pady=10)

# Botón para salir
btn_salir = tk.Button(root, text="Salir", command=root.quit)
btn_salir.pack(pady=5)

# Ejecutar la aplicación
root.mainloop()
