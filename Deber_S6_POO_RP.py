class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def presentarse(self):
        return f"hola, soy {self.nombre} {self.apellido}, y tengo {self.edad} de edad."


class Estudiante(Persona):
    def __init__(self, nombre, apellido, edad, grado):
        super().__init__(nombre, apellido, edad)
        self.grado = grado
        self.__calificacion_promedio_ = 0.0

    def estudiar(self):
        return f"{self.nombre} está estudiando en el {self.grado}."

    def calcular_promedio(self, notas):
        self.__calificacion_promedio = sum(notas) / len(notas)

    def obtener_promedios(self):
        return f"El promedio de {self.nombre} {self.apellido} es de {self.__calificacion_promedio:.2f}"


class Profesor(Persona):
    def __init__(self, nombre, apellido, edad, materia):
        super().__init__(nombre, apellido, edad)
        self.materia = materia
        self.__materia_impartida_ = "lenguaje"

    def materiaimpartida(self):
        return f"{self.nombre} {self.apellido} tiene {self.edad} y da la materia de {self.materia}."


estudiante1 = Estudiante("Luis", "Cisneros", 15, "8vo")
profesor1 = Profesor("Ronald", "Piedra", 33, "lenguaje")

print(estudiante1.presentarse())
print(estudiante1.estudiar())

notas = [8.5, 9.7, 10, 8]
estudiante1.calcular_promedio(notas)
print(estudiante1.obtener_promedios())
print(profesor1.materiaimpartida())