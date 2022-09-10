"""
Crea una clase llamada Cuenta que tendrá los siguientes atributos:
- titular (que es una persona)
- cantidad (puede tener decimales).

El titular será obligatorio y la cantidad es opcional en el constructor.

Construye los siguientes métodos para la clase:
Un constructor, donde los datos pueden estar vacíos.

- mostrar(): Imprimir por pantalla los datos de la cuenta.

- ingresar(cantidad): se ingresa una cantidad a la cuenta,
  si la cantidad introducida es negativa, no se hará nada.

- retirar(cantidad): se retira una cantidad a la cuenta.

La cuenta puede estar en números rojos.
"""


class Cuenta:

    def __init__(self, titular, cantidad=0):
        self.titular = titular
        self.cantidad = cantidad

    def mostrar(self):
        print(f'Titular: {self.titular}, Cantidad: {self.cantidad}')

    def ingresar(self, monto):
        if monto > 0:
            self.cantidad = self.cantidad + monto

    def retirar(self, monto):
        if monto <= self.cantidad and monto > 0:
            self.cantidad = self.cantidad - monto
        else:
            print('Fondos insuficientes')


# Programa principal

nombre = input('Ingrese nombre: ')
monto_inicial = float(input('Ingrese monto inicial: '))

cuentaCorriente = Cuenta(nombre, monto_inicial)
cuentaCorriente.ingresar(1000)
cuentaCorriente.mostrar()
cuentaCorriente.retirar(600)
cuentaCorriente.mostrar()
