class Motocicleta:
    def __init__(self, color, patente, modelo):
        self.color = color
        self.patente = patente
        self.modelo = modelo
        self.estado = False

    def apagar(self):
        if (self.estado == True):
            self.estado = False

    def encender(self):
        if (self.estado == False):
            self.estado = True

# Programa principal

yamaha = Motocicleta()  
print(yamaha.estado)
yamaha.encender()
print(yamaha.estado)
yamaha.apagar()
print(yamaha.estado)
