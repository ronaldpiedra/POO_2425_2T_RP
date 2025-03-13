import json  # Importamos la librería para guardar y cargar datos en un archivo JSON

class Libro:
    def __init__(self, id, titulo, autor, genero, cantidad):
        """
        Constructor de la clase Libro.
        Cada libro tiene un ID, título, autor, género y cantidad disponible.
        """
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.cantidad = cantidad

    def to_dict(self):
        """
        Convierte el objeto en un diccionario para poder almacenarlo en un archivo JSON.
        """
        return {
            "id": self.id,
            "titulo": self.titulo,
            "autor": self.autor,
            "genero": self.genero,
            "cantidad": self.cantidad
        }


class Biblioteca:
    def __init__(self):
        """
        Constructor de la clase Biblioteca.
        Usamos un diccionario para almacenar los libros, donde la clave es el ID del libro.
        """
        self.libros = {}

    def agregar_libro(self, libro):
        """
        Agrega un nuevo libro a la biblioteca.
        """
        if libro.id in self.libros:
            print("⚠️ El libro ya existe en la biblioteca.")
        else:
            self.libros[libro.id] = libro
            print(f"✅ Libro '{libro.titulo}' agregado con éxito.")

    def eliminar_libro(self, id):
        """
        Elimina un libro por su ID.
        """
        if id in self.libros:
            libro = self.libros.pop(id)  # Remueve y devuelve el libro eliminado
            print(f"🗑️ Libro '{libro.titulo}' eliminado correctamente.")
        else:
            print("❌ No se encontró un libro con ese ID.")

    def buscar_libro(self, id):
        """
        Busca un libro por su ID y muestra su información.
        """
        if id in self.libros:
            libro = self.libros[id]
            print(f"📖 {libro.titulo} - {libro.autor} (Género: {libro.genero}, Cantidad: {libro.cantidad})")
        else:
            print("🔍 No se encontró un libro con ese ID.")

    def mostrar_libros(self):
        """
        Muestra todos los libros disponibles en la biblioteca.
        """
        if not self.libros:
            print("📚 La biblioteca está vacía.")
        else:
            print("📚 Lista de libros:")
            for libro in self.libros.values():
                print(f"📖 {libro.titulo} - {libro.autor} (ID: {libro.id}, Cantidad: {libro.cantidad})")

    def prestar_libro(self, id):
        """
        Permite prestar un libro si hay ejemplares disponibles.
        """
        if id in self.libros:
            if self.libros[id].cantidad > 0:
                self.libros[id].cantidad -= 1
                print(f"📕 Has prestado '{self.libros[id].titulo}'.")
            else:
                print("❌ No hay ejemplares disponibles.")
        else:
            print("🔍 No se encontró el libro.")

    def devolver_libro(self, id):
        """
        Permite devolver un libro prestado, aumentando la cantidad disponible.
        """
        if id in self.libros:
            self.libros[id].cantidad += 1
            print(f"📘 Has devuelto '{self.libros[id].titulo}'.")
        else:
            print("🔍 No se encontró el libro.")

    def guardar_en_archivo(self, archivo="biblioteca.json"):
        """
        Guarda el estado de la biblioteca en un archivo JSON.
        """
        with open(archivo, "w") as f:
            json.dump({id: libro.to_dict() for id, libro in self.libros.items()}, f)
        print("💾 Biblioteca guardada en archivo.")

    def cargar_desde_archivo(self, archivo="biblioteca.json"):
        """
        Carga los datos de la biblioteca desde un archivo JSON.
        """
        try:
            with open(archivo, "r") as f:
                datos = json.load(f)
                self.libros = {id: Libro(**info) for id, info in datos.items()}
            print("📂 Biblioteca cargada desde archivo.")
        except FileNotFoundError:
            print("⚠️ No se encontró el archivo, iniciando biblioteca vacía.")


def menu():
    """
    Función que muestra un menú interactivo para gestionar la biblioteca.
    """
    biblioteca = Biblioteca()
    biblioteca.cargar_desde_archivo()

    while True:
        print("\n📚 Menú Biblioteca")
        print("1️⃣ Agregar libro")
        print("2️⃣ Eliminar libro")
        print("3️⃣ Buscar libro")
        print("4️⃣ Mostrar todos los libros")
        print("5️⃣ Prestar libro")
        print("6️⃣ Devolver libro")
        print("7️⃣ Guardar y salir")

        opcion = input("🔹 Elige una opción: ")

        if opcion == "1":
            id = input("🆔 ID del libro: ")
            titulo = input("📖 Título: ")
            autor = input("✍️ Autor: ")
            genero = input("📚 Género: ")
            cantidad = int(input("📦 Cantidad disponible: "))
            libro = Libro(id, titulo, autor, genero, cantidad)
            biblioteca.agregar_libro(libro)

        elif opcion == "2":
            id = input("🆔 ID del libro a eliminar: ")
            biblioteca.eliminar_libro(id)

        elif opcion == "3":
            id = input("🆔 ID del libro a buscar: ")
            biblioteca.buscar_libro(id)

        elif opcion == "4":
            biblioteca.mostrar_libros()

        elif opcion == "5":
            id = input("🆔 ID del libro a prestar: ")
            biblioteca.prestar_libro(id)

        elif opcion == "6":
            id = input("🆔 ID del libro a devolver: ")
            biblioteca.devolver_libro(id)

        elif opcion == "7":
            biblioteca.guardar_en_archivo()
            print("👋 ¡Hasta luego!")
            break

        else:
            print("⚠️ Opción no válida, intenta de nuevo.")


# Ejecutar el menú solo si el script se ejecuta directamente
if __name__ == "__main__":
    menu()
