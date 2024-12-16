# Clase que representa a un Libro en la biblioteca
class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True

    def mostrar_info(self):
        return f"{self.titulo} de {self.autor}, ISBN: {self.isbn}"

    def marcar_como_prestado(self):
        self.disponible = False

    def marcar_como_disponible(self):
        self.disponible = True

# Clase que representa a un Usuario de la biblioteca
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def pedir_libro(self, libro):
        if libro.disponible:
            libro.marcar_como_prestado()
            self.libros_prestados.append(libro)
            return f"El libro '{libro.titulo}' ha sido prestado a {self.nombre}."
        else:
            return f"El libro '{libro.titulo}' no está disponible en este momento."

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            libro.marcar_como_disponible()
            self.libros_prestados.remove(libro)
            return f"{self.nombre} ha devuelto el libro '{libro.titulo}'."
        else:
            return f"{self.nombre} no tiene el libro '{libro.titulo}'."

# Clase que representa la Biblioteca, con una colección de libros y usuarios
class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def mostrar_libros_disponibles(self):
        disponibles = [libro.mostrar_info() for libro in self.libros if libro.disponible]
        return disponibles

# Ejemplo de uso del sistema
biblioteca = Biblioteca()

# Crear libros
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "978-3-16-148410-0")
libro2 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "978-3-16-148411-7")
libro3 = Libro("1984", "George Orwell", "978-0-452-28423-4")

# Agregar libros a la biblioteca
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)

# Crear un usuario
usuario1 = Usuario("Juan Pérez", 101)

# Registrar usuario en la biblioteca
biblioteca.registrar_usuario(usuario1)

# Mostrar libros disponibles
print("Libros disponibles en la biblioteca:")
for libro in biblioteca.mostrar_libros_disponibles():
    print(libro)

# El usuario pide prestado un libro
print(usuario1.pedir_libro(libro1))

# Mostrar libros disponibles después de un préstamo
print("\nLibros disponibles después del préstamo:")
for libro in biblioteca.mostrar_libros_disponibles():
    print(libro)

# El usuario devuelve el libro
print(usuario1.devolver_libro(libro1))

# Mostrar libros disponibles después de la devolución
print("\nLibros disponibles después de la devolución:")
for libro in biblioteca.mostrar_libros_disponibles():
    print(libro)
