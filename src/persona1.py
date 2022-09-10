"""
Crear una clase llamada Persona.
Sus atributos son: nombre, edad y DNI. Ingresar dichos atributos por pantalla (consola)
Construye los siguientes métodos para la clase:
mostrar(): Muestra los datos de la persona por pantalla (consola)
esMayorDeEdad(): Devuelve un valor lógico (booleano) indicando si es mayor de edad.
"""


class Persona:
    nombre = ''
    edad = 0
    dni = 0

    def mostrar(self):
        print('Nombre: ' + self.nombre)
        print('Edad: ' + str(self.edad))
        print('DNI: ' + str(self.dni))

    def esMayorDeEdad(self):
        if (self.edad >= 18):
            return True
        else:
            return False


juan = Persona()
nombre = input('Ingrese un nombre: ')
edad = int(input('Ingrese edad: '))
juan.nombre = nombre
juan.edad = edad
juan.dni = int(input('Ingrese DNI: '))
juan.mostrar()
respuesta = juan.esMayorDeEdad()
print('Es mayor de edad: ' + str(respuesta))
