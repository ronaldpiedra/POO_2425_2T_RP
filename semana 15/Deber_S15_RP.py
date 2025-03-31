import tkinter as tk
from tkinter import messagebox

# Función para agregar tarea
def agregar_tarea():
    tarea = entrada.get().strip()  # Obtener tarea del campo de entrada
    if tarea:
        lista_tareas.insert(tk.END, tarea)
        entrada.delete(0, tk.END)  # Limpiar campo de entrada
    else:
        messagebox.showwarning("Entrada Vacía", "Por favor, ingrese una tarea.")

# Función para marcar tarea como completada
def marcar_completada():
    try:
        # Obtener tarea seleccionada
        tarea_seleccionada = lista_tareas.curselection()
        if tarea_seleccionada:
            tarea = lista_tareas.get(tarea_seleccionada)
            # Cambiar color de la tarea para indicar que está completada
            lista_tareas.itemconfig(tarea_seleccionada, {'bg':'light green'})
            lista_tareas.selection_clear(0, tk.END)  # Limpiar selección
        else:
            messagebox.showwarning("Selección Vacía", "Por favor, seleccione una tarea para marcar como completada.")
    except Exception as e:
        print(f"Error al marcar como completada: {e}")

# Función para eliminar tarea
def eliminar_tarea():
    try:
        tarea_seleccionada = lista_tareas.curselection()
        if tarea_seleccionada:
            lista_tareas.delete(tarea_seleccionada)
        else:
            messagebox.showwarning("Selección Vacía", "Por favor, seleccione una tarea para eliminar.")
    except Exception as e:
        print(f"Error al eliminar tarea: {e}")

# Función para permitir agregar tarea con Enter
def presionar_enter(event):
    agregar_tarea()

# Crear la ventana principal
root = tk.Tk()
root.title("Lista de Tareas")
root.geometry("400x400")

# Campo de entrada
entrada = tk.Entry(root, width=40, bg="light yellow")
entrada.pack(pady=10)

# Lista de tareas
lista_tareas = tk.Listbox(root, width=40, height=10, selectmode=tk.SINGLE)
lista_tareas.pack(pady=10)

# Botones
boton_agregar = tk.Button(root, text="Añadir Tarea", command=agregar_tarea)
boton_agregar.pack(pady=5)

boton_completar = tk.Button(root, text="Marcar como Completada", command=marcar_completada)
boton_completar.pack(pady=5)

boton_eliminar = tk.Button(root, text="Eliminar Tarea", command=eliminar_tarea)
boton_eliminar.pack(pady=5)

# Enlazar tecla Enter para agregar tarea
root.bind('<Return>', presionar_enter)

# Iniciar la ventana
root.mainloop()