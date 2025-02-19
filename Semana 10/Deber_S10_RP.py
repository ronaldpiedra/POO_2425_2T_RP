class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio


class Inventario:
    def __init__(self):
        #"inizializa la lista de los productos la cual está vacía"
        self.productos = []
        self.cargar_desde_archivo()

    def agregar_producto(self, producto):
        self.productos.append(producto)
        print(f"Producto '{producto.nombre}' agregado exitosamente.")

    def mostrar_productos(self):
        if not self.productos:
            print("No hay productos en el inventario:")
        else:
            print("la lista de los productos si está en el inventario")
            for producto in self.productos:
                print(
                    f"id:{producto.id}, Nombre: {producto.nombre}, Cantidad: {producto.cantidad}, Precio: {producto.precio}")

    def guardar_en_archivo(self, nombre_archivo="inventario_S10.txt"):
        try:
            with open(nombre_archivo, "w") as archivo:
                for producto in self.productos:
                    archivo.write(f"{producto.id}, {producto.nombre}, {producto.cantidad}, {producto.precio}\n")
            print("Inventario guardado correctamente")
        except PermissionError:
            print("Error: no tienes permisos para escribir aquí.")

    def cargar_desde_archivo(self, nombre_archivo="inventario_S10.txt"):
        try:
            with open(nombre_archivo, "r") as archivo:
                for linea in archivo:
                    datos = [dato.strip() for dato in linea.strip().split(",")]
                    if len(datos) == 4:
                        id, nombre, cantidad, precio = datos
                        self.productos.append(Producto(int(id), nombre, int(cantidad), float(precio)))
            print("Su inventario está cargado correctamente desde el archivo en su pc")
        except FileNotFoundError:
            print("Hubo un error al cargar su archivo desde la pc, se inicia el inventario vacio")
        except ValueError:
            print("Hubo un error al leer los datos del archivo desde su pc, verifique el fotmato del archivo")

inventario = Inventario()
inventario.agregar_producto(Producto(1, "Celular", 2, 1400))
inventario.agregar_producto(Producto(2, "Reloj", 4, 200))
inventario.agregar_producto(Producto(3, "Cámara", 1, 16.06))
inventario.agregar_producto(Producto(4, "Goku", 1, 20))


inventario.guardar_en_archivo()

inventario_nuevo = Inventario()

inventario_nuevo.mostrar_productos()