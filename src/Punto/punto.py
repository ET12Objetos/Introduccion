"""""
Realizar un programa que dado un punto en el plano (con coordenadas x e y) cartesiano me informe por pantalla en que cuadrante se encuentra  
y ademas la distancia entre dicho punto y al origen.
"""
import math
""


class Punto:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def informarCuadrante(self):
        if self.__x > 0 and self.__y > 0:
            print('Cuadrante I')
        elif self.__x < 0 and self.__y > 0:
            print('Cuadrante II')
        elif self.__x < 0 and self.__y < 0:
            print('cuadrante III')
        elif self.__x > 0 and self.__y < 0:
            print('Cuadrante IV')

    def distancia(self):
        distancia = math.sqrt(self.__x ** 2 + self.__y ** 2)
        print(f'La distancia es {distancia}')

    def distancia(self, punto):
        distancia = math.sqrt((self.__x - punto.__x) **
                              2 + (self.__y - punto.__y) ** 2)
        print(f'La distancia es {distancia}')
