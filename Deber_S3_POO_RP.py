Programación tradicional


def ingresar_temperaturas():
    """Solicita al usuario las temperaturas diarias de la semana"""
    temperaturas = []
    for i in range(7):
        temperatura = float(input(f"Ingrese la temperatura del día {i + 1}: "))
        temperaturas.append(temperatura)
    return temperaturas

def calcular_promedio(temperaturas):
    """Calcula el promedio de las temperaturas"""
    return sum(temperaturas) / len(temperaturas)

def mostrar_resultado(promedio):
    """Muestra el resultado del cálculo"""
    print(f"El promedio semanal de las temperaturas es: {promedio:.2f} °C")

# Función principal para ejecutar el programa
def main():
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)
    mostrar_resultado(promedio)

if __name__ == "__main__":
    main()


Programación POO


class Clima:
    def __init__(self):
        """Inicializa la lista de temperaturas de la semana"""
        self.temperaturas = []

    def ingresar_temperaturas(self):
        """Solicita al usuario las temperaturas diarias de la semana"""
        for i in range(7):
            temperatura = float(input(f"Ingrese la temperatura del día {i + 1}: "))
            self.temperaturas.append(temperatura)

    def calcular_promedio(self):
        """Calcula el promedio de las temperaturas"""
        return sum(self.temperaturas) / len(self.temperaturas)

    def mostrar_resultado(self):
        """Muestra el resultado del cálculo"""
        promedio = self.calcular_promedio()
        print(f"El promedio semanal de las temperaturas es: {promedio:.2f} °C")

# Función principal para ejecutar el programa
def main():
    clima = Clima()  # Crear una instancia de la clase Clima
    clima.ingresar_temperaturas()  # Ingresar las temperaturas
    clima.mostrar_resultado()  # Mostrar el resultado del promedio

if __name__ == "__main__":
    main()

#Comentario

Ambos enfoques, tanto la Programación Tradicional como la Orientada a Objetos (POO), resuelven el cálculo del promedio de las temperaturas semanales, pero de forma distinta. 
 En la programación tradicional, se emplean funciones para organizar el código y manejar las entradas de forma secuencial. En la POO, la lógica se encapsula dentro de una clase, lo que facilita futuras modificaciones, como agregar atributos o métodos adicionales. 
La POO promueve la reutilización y modularidad del código, lo que lo hace más flexible y fácil de mantener.
