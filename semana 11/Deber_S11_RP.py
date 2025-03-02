class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def to_dict(self):
        return {"id": self.id, "nombre": self.nombre, "cantidad": self.cantidad, "precio": self.precio}

class Inventario:
    def __init__(self, archivo="inventario.json"):
        self.archivo = archivo
        self.productos = {}
        self.cargar_desde_archivo()

    def agregar_producto(self, producto):
        if producto.id in self.productos:
            print("El ID ya existe. Usa actualizar producto en su lugar.")
        else:
            self.productos[producto.id] = producto
            print(f"Producto '{producto.nombre}' agregado exitosamente.")

    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]
            print("Producto eliminado correctamente.")
        else:
            print("Producto no encontrado.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        if id in self.productos:
            if cantidad is not None:
                self.productos[id].cantidad = cantidad
            if precio is not None:
                self.productos[id].precio = precio
            print("Producto actualizado correctamente.")
        else:
            print("Producto no encontrado.")

    def buscar_producto(self, nombre):
        encontrados = [p for p in self.productos.values() if p.nombre.lower() == nombre.lower()]
        if encontrados:
            for p in encontrados:
                print(f"ID: {p.id}, Nombre: {p.nombre}, Cantidad: {p.cantidad}, Precio: {p.precio}")
        else:
            print("Producto no encontrado.")

    def mostrar_productos(self):
        if not self.productos:
            print("No hay productos en el inventario.")
        else:
            print("Lista de productos en el inventario:")
            for p in self.productos.values():
                print(f"ID: {p.id}, Nombre: {p.nombre}, Cantidad: {p.cantidad}, Precio: {p.precio}")

    def guardar_en_archivo(self):
        try:
            with open(self.archivo, "w") as archivo:
                json.dump({id: p.to_dict() for id, p in self.productos.items()}, archivo)
            print("Inventario guardado correctamente.")
        except PermissionError:
            print("Error: No tienes permisos para escribir aquí.")

    def cargar_desde_archivo(self):
        try:
            with open(self.archivo, "r") as archivo:
                datos = json.load(archivo)
                self.productos = {int(id): Producto(int(id), p["nombre"], p["cantidad"], p["precio"]) for id, p in datos.items()}
            print("Inventario cargado correctamente.")
        except FileNotFoundError:
            print("Inventario no encontrado. Se inicia con un inventario vacío.")
        except json.JSONDecodeError:
            print("Error al leer el archivo. Verifique el formato JSON.")

# Menú interactivo
def menu():
    inventario = Inventario()
    while True:
        print("\n1. Agregar Producto")
        print("2. Eliminar Producto")
        print("3. Actualizar Producto")
        print("4. Buscar Producto")
        print("5. Mostrar Productos")
        print("6. Guardar y Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id = int(input("ID: "))
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.agregar_producto(Producto(id, nombre, cantidad, precio))

        elif opcion == "2":
            id = int(input("ID del producto a eliminar: "))
            inventario.eliminar_producto(id)

        elif opcion == "3":
            id = int(input("ID del producto a actualizar: "))
            cantidad = input("Nueva cantidad (dejar vacío para no cambiar): ")
            precio = input("Nuevo precio (dejar vacío para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id, cantidad, precio)

        elif opcion == "4":
            nombre = input("Nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == "5":
            inventario.mostrar_productos()

        elif opcion == "6":
            inventario.guardar_en_archivo()
            print("Saliendo...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    menu()