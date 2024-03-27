def solicitar_datos():
    nombre = input("Por favor, ingresa tu nombre: ")
    apellido = input("Por favor, ingresa tu apellido: ")
    edad = input("Por favor, ingresa tu edad: ")
    sede = input("Por favor, ingresa tu sede: ")
    return nombre, apellido, edad, sede

def imprimir_datos(nombre, apellido, edad, sede):
    print("Datos ingresados:")
    print("Nombre:", nombre)
    print("Apellido:", apellido)
    print("Edad:", edad)
    print("Sede:", sede)

def main():
    nombre, apellido, edad, sede = solicitar_datos()
    imprimir_datos(nombre, apellido, edad, sede)

if __name__ == "__main__":
    main()

