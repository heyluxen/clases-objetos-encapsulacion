class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0.0):
        self._titular = titular
        self._saldo = saldo_inicial

    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, nuevo_saldo):
        if nuevo_saldo < 0:
            raise ValueError("El saldo no puede ser negativo")
        self._saldo = nuevo_saldo

    def depositar(self, cantidad):
        if cantidad > 0:
            self._saldo += cantidad
            return True
        return False

    def retirar(self, cantidad):
        if 0 < cantidad <= self._saldo:
            self._saldo -= cantidad
            return True
        return False

# Prueba
if __name__ == "__main__":
    cuenta = CuentaBancaria("Ana Pérez", 1000.0)
    print(f"Titular: {cuenta.titular}")
    print(f"Saldo inicial: {cuenta.saldo}")

    if cuenta.depositar(500):
        print(f"Depósito exitoso. Nuevo saldo: {cuenta.saldo}")
    else:
        print("Depósito no válido")

    if cuenta.retirar(200):
        print(f"Retiro exitoso. Nuevo saldo: {cuenta.saldo}")
    else:
        print("Retiro no válido")

    try:
        cuenta.saldo = -100
    except ValueError as e:
        print(f"Error: {e}")