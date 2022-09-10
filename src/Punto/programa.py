from punto import Punto

coordenada_x = int(input('Ingrese la coordenada x: '))
coordenada_y = int(input('Ingrese la coordenada y: '))

punto = Punto(coordenada_x, coordenada_y)

punto.informarCuadrante()
# punto.distancia()
punto.distancia(Punto(1, 1))
