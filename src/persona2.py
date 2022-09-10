"""
Crear una clase llamada Persona.
Sus atributos son: nombre, edad y DNI. 
Realizar los getters y setters de cada atributo
Ingresar dichos atributos por pantalla (consola)
Construye los siguientes métodos para la clase:
mostrar(): Muestra los datos de la persona por pantalla (consola)
esMayorDeEdad(): Devuelve un valor lógico (booleano) indicando si es mayor de edad.
"""

class Persona:

    # __nombre es un atributo publico y __edad es un atributo privado
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.__edad = edad

    # método getter obtiene el valor de 'edad'
    @property
    def edad(self):
        return self.__edad

    # método setter establece el valor de 'edad'
    @edad.setter
    def edad(self, una_edad):
        if (una_edad <= 0):
            print("La edad no es valida")
        else:
            self.__edad = una_edad


persona = Persona('Juan', 25)
persona.edad = 15
print(persona.edad)
