# Programa de conversión de temperatura
# Este programa permite convertir una temperatura en grados Celsius a Fahrenheit y viceversa.

# Definimos las funciones para la conversión
def celsius_a_fahrenheit(celsius):
    """
    Convierte la temperatura de Celsius a Fahrenheit.

    Parámetro:
    celsius (float): Temperatura en grados Celsius.

    Retorna:
    float: Temperatura convertida a grados Fahrenheit.
    """
    return (celsius * 9 / 5) + 32


def fahrenheit_a_celsius(fahrenheit):
    """
    Convierte la temperatura de Fahrenheit a Celsius.

    Parámetro:
    fahrenheit (float): Temperatura en grados Fahrenheit.

    Retorna:
    float: Temperatura convertida a grados Celsius.
    """
    return (fahrenheit - 32) * 5 / 9


# Función principal que gestiona la entrada y salida
def main():
    # Entrada del usuario
    tipo_conversion = input("Elija el tipo de conversión (1 para Celsius a Fahrenheit, 2 para Fahrenheit a Celsius): ")

    if tipo_conversion == "1":
        celsius = float(input("Ingrese la temperatura en grados Celsius: "))
        fahrenheit = celsius_a_fahrenheit(celsius)
        print(f"{celsius}° Celsius es igual a {fahrenheit}° Fahrenheit.")
    elif tipo_conversion == "2":
        fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))
        celsius = fahrenheit_a_celsius(fahrenheit)
        print(f"{fahrenheit}° Fahrenheit es igual a {celsius}° Celsius.")
    else:
        print("Opción no válida. Por favor, elija 1 o 2.")


# Llamamos a la función principal para ejecutar el programa
if __name__ == "__main__":
    main()
