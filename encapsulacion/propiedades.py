# =============================================
# PROPIEDADES CON @property
# =============================================

class Temperatura:
    def __init__(self, celsius=0):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, valor):
        if valor < -273.15:
            raise ValueError("Menor que cero absoluto")
        self._celsius = valor

    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32

    @fahrenheit.setter
    def fahrenheit(self, valor):
        c = (valor - 32) * 5/9
        if c < -273.15:
            raise ValueError("Menor que cero absoluto")
        self._celsius = c

temp = Temperatura(25)
print("=== PROPIEDADES ===")
print(f"{temp.celsius}°C = {temp.fahrenheit}°F")
temp.celsius = 30
print(f"{temp.celsius}°C = {temp.fahrenheit}°F")
temp.fahrenheit = 68
print(f"{temp.celsius}°C = {temp.fahrenheit}°F")
print()

# Propiedad de solo lectura (Círculo)
import math
class Circulo:
    def __init__(self, radio):
        self._radio = radio

    @property
    def radio(self):
        return self._radio

    @radio.setter
    def radio(self, valor):
        if valor <= 0:
            raise ValueError("Radio positivo")
        self._radio = valor

    @property
    def area(self):
        return math.pi * self._radio ** 2

    @property
    def perimetro(self):
        return 2 * math.pi * self._radio

c = Circulo(5)
print("=== PROPIEDADES SOLO LECTURA ===")
print(f"Radio: {c.radio}, Área: {c.area:.2f}")
c.radio = 10
print(f"Nuevo radio: {c.radio}, Nueva área: {c.area:.2f}")
# c.area = 100  # AttributeError
print()

# Propiedad calculada (Empleado)
class Empleado:
    def __init__(self, nombre, salario_base, horas_extra=0, tarifa_extra=0):
        self._nombre = nombre
        self._salario_base = salario_base
        self._horas_extra = horas_extra
        self._tarifa_extra = tarifa_extra

    @property
    def salario_total(self):
        return self._salario_base + self._horas_extra * self._tarifa_extra

    @property
    def horas_extra(self):
        return self._horas_extra

    @horas_extra.setter
    def horas_extra(self, valor):
        self._horas_extra = valor

e = Empleado("Laura", 2000, 10, 15)
print("Salario total:", e.salario_total)
e.horas_extra = 15
print("Nuevo salario total:", e.salario_total)