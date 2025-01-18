
class Persona:
    def __init__(self, nombre, apellido, edad):
        """
        Constructor que inicializa los atributos de la clase Persona.
        """
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def __del__(self):
        """
        Destructor que se llama cuando el objeto de la clase Persona es destruido.
        Aquí puedes realizar limpieza de recursos si es necesario.
        """
        print(f"Objeto {self.nombre} {self.apellido} eliminado.")

    def presentarse(self):
        return f"Hola, soy {self.nombre} {self.apellido}, y tengo {self.edad} años."


class Estudiante(Persona):
    def __init__(self, nombre, apellido, edad, grado):
        """
        Constructor que inicializa los atributos de la clase Estudiante.
        Hereda de la clase Persona.
        """
        super().__init__(nombre, apellido, edad)
        self.grado = grado
        self.__calificacion_promedio_ = 0.0

    def __del__(self):
        """
        Destructor específico para la clase Estudiante.
    .
        """
        print(f"Estudiante {self.nombre} {self.apellido} eliminado.")
        super().__del__()

    def estudiar(self):
        return f"{self.nombre} está estudiando en el {self.grado}."

    def calcular_promedio(self, notas):
        self.__calificacion_promedio = sum(notas) / len(notas)

    def obtener_promedios(self):
        return f"El promedio de {self.nombre} {self.apellido} es de {self.__calificacion_promedio:.2f}"


class Profesor(Persona):
    def __init__(self, nombre, apellido, edad, materia):
        """
        Constructor que inicializa los atributos de la clase Profesor.
        Hereda de la clase Persona.
        """
        super().__init__(nombre, apellido, edad)
        self.materia = materia
        self.__materia_impartida_ = "lenguaje"

    def __del__(self):
        """
        Destructor específico para la clase Profesor.

        """
        print(f"Profesor {self.nombre} {self.apellido} eliminado.")
        super().__del__()

    def materiaimpartida(self):
        return f"{self.nombre} {self.apellido} tiene {self.edad} y da la materia de {self.materia}."


# Crear instancias de las clases
estudiante1 = Estudiante("Luis", "Cisneros", 15, "8vo")
profesor1 = Profesor("Ronald", "Piedra", 33, "Lenguaje")

# Imprimir métodos de las instancias
print(estudiante1.presentarse())
print(estudiante1.estudiar())

notas = [8.5, 9.7, 10, 8]
estudiante1.calcular_promedio(notas)
print(estudiante1.obtener_promedios())
print(profesor1.materiaimpartida())

# Eliminar objetos explícitamente para llamar al destructor
del estudiante1
del profesor1
