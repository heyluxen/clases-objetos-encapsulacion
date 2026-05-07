class CuentaBancaria:
    def __init__(self, titular, saldo_inicial, pin):
        self._titular = titular          # protegido (convención)
        self._saldo = saldo_inicial      # protegido
        self.__pin = pin                 # privado (name mangling)

    def depositar(self, cantidad):
        if cantidad > 0:
            self._saldo += cantidad
            return True
        return False

    def validar_pin(self, pin_ingresado):
        return self.__pin == pin_ingresado

cuenta = CuentaBancaria("Ana García", 1000, "1234")
print("=== ATRIBUTOS PRIVADOS ===")
print("Saldo (acceso no recomendado):", cuenta._saldo)
# print(cuenta.__pin)  # AttributeError
print("¿Pin válido?", cuenta.validar_pin("1234"))
print()

# Ejemplo de name mangling
print("Nombre real del atributo privado:", dir(cuenta)[-1])  # _CuentaBancaria__pin
print("Acceso mediante name mangling:", cuenta._CuentaBancaria__pin)
print()

# Atributos protegidos en herencia
class Vehiculo:
    def __init__(self, marca, modelo):
        self._marca = marca      # protegido
        self.__modelo = modelo   # privado

class Coche(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self._puertas = puertas
    def info(self):
        print("Marca (protegido):", self._marca)
        # print(self.__modelo)  # error

v = Coche("Toyota", "Corolla", 4)
v.info()