import tkinter as tk
from tkinter import messagebox

# Función para añadir tarea
def agregar_tarea():
    tarea = entrada.get().strip()
    if tarea:
        lista_tareas.insert(tk.END, tarea)
        entrada.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Por favor, ingrese una tarea.")

# Función para marcar tarea como completada
def marcar_completada():
    tarea_seleccionada = lista_tareas.curselection()
    if tarea_seleccionada:
        tarea = lista_tareas.get(tarea_seleccionada)
        lista_tareas.delete(tarea_seleccionada)
        lista_tareas.insert(tk.END, f"[Completada] {tarea}")
    else:
        messagebox.showwarning("Advertencia", "Seleccione una tarea para marcar como completada.")

# Función para eliminar tarea
def eliminar_tarea():
    tarea_seleccionada = lista_tareas.curselection()
    if tarea_seleccionada:
        lista_tareas.delete(tarea_seleccionada)
    else:
        messagebox.showwarning("Advertencia", "Seleccione una tarea para eliminar.")

# Función para cerrar la aplicación
def cerrar_app(event=None):
    root.quit()

# Configuración de la ventana principal
root = tk.Tk()
root.title("Gestión de Tareas")
root.geometry("500x400")

# Entrada para nuevas tareas
entrada = tk.Entry(root, width=40)
entrada.pack(pady=10)

# Lista de tareas
lista_tareas = tk.Listbox(root, width=40, height=10, selectmode=tk.SINGLE)
lista_tareas.pack(pady=10)

# Botones
btn_agregar = tk.Button(root, text="Añadir Tarea", width=20, command=agregar_tarea)
btn_agregar.pack(pady=5)

btn_completar = tk.Button(root, text="Marcar como Completada", width=20, command=marcar_completada)
btn_completar.pack(pady=5)

btn_eliminar = tk.Button(root, text="Eliminar Tarea", width=20, command=eliminar_tarea)
btn_eliminar.pack(pady=5)

# Atajos de teclado
root.bind("<Return>", lambda event: agregar_tarea())  # Tecla Enter para añadir tarea
root.bind("<c>", lambda event: marcar_completada())  # Tecla 'C' para marcar como completada
root.bind("<Delete>", lambda event: eliminar_tarea())  # Tecla Delete para eliminar tarea
root.bind("<Escape>", lambda event: cerrar_app())  # Tecla Escape para cerrar la app

# Ejecutar la aplicación
root.mainloop()
