# =============================================
# MÉTODOS DE INSTANCIA, ESTÁTICOS, DE CLASE
# =============================================

# Métodos de instancia básicos
class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = 0
        self.encendido = False

    def encender(self):
        if not self.encendido:
            self.encendido = True
            return f"{self.marca} {self.modelo} encendido"
        return f"{self.marca} {self.modelo} ya estaba encendido"

    def apagar(self):
        if self.encendido:
            self.encendido = False
            self.velocidad = 0
            return f"{self.marca} {self.modelo} apagado"
        return f"{self.marca} {self.modelo} ya estaba apagado"

mi_coche = Coche("Toyota", "Corolla")
print("=== MÉTODOS BÁSICOS ===")
print(mi_coche.encender())
print(mi_coche.apagar())
print()

# Métodos con parámetros (acelerar/frenar)
class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = 0
        self.encendido = False
        self.velocidad_maxima = 200

    def acelerar(self, incremento):
        if not self.encendido:
            return "Coche apagado"
        nueva = self.velocidad + incremento
        if nueva > self.velocidad_maxima:
            self.velocidad = self.velocidad_maxima
        else:
            self.velocidad = nueva
        return f"Velocidad: {self.velocidad} km/h"

    def frenar(self, decremento):
        if self.velocidad == 0:
            return "Detenido"
        nueva = self.velocidad - decremento
        self.velocidad = max(nueva, 0)
        return f"Velocidad: {self.velocidad} km/h"

c = Coche("Toyota", "Corolla")
c.encender = lambda: None  # simplificación, pero se entiende
c.encendido = True
print("=== MÉTODOS CON PARÁMETROS ===")
print(c.acelerar(50))
print(c.frenar(30))
print()

# Métodos con valores de retorno (Calculadora)
class Calculadora:
    def sumar(self, a, b): return a + b
    def restar(self, a, b): return a - b
    def multiplicar(self, a, b): return a * b
    def dividir(self, a, b): return a / b if b != 0 else "Error"
    def calcular_estadisticas(self, numeros):
        if not numeros:
            return {"suma": 0, "promedio": 0, "minimo": None, "maximo": None}
        return {
            "suma": sum(numeros),
            "promedio": sum(numeros)/len(numeros),
            "minimo": min(numeros),
            "maximo": max(numeros)
        }

calc = Calculadora()
print("=== MÉTODOS QUE DEVUELVEN VALORES ===")
print(calc.sumar(5,3))
print(calc.calcular_estadisticas([4,7,2,9,5]))
print()

# Métodos que llaman a otros métodos
class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"
    def es_mayor_de_edad(self):
        return self.edad >= 18
    def presentarse(self):
        estado = "mayor" if self.es_mayor_de_edad() else "menor"
        return f"Soy {self.nombre_completo()} y soy {estado}"

p = Persona("Juan", "Pérez", 25)
print("=== MÉTODOS QUE LLAMAN A OTROS ===")
print(p.presentarse())
print()

# Métodos de clase y estáticos
class MathUtils:
    @staticmethod
    def es_primo(n):
        if n < 2: return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0: return False
        return True

class Empleado:
    num_empleados = 0
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
        Empleado.num_empleados += 1
    @classmethod
    def desde_salario_anual(cls, nombre, salario_anual):
        return cls(nombre, salario_anual / 12)
    @classmethod
    def total_empleados(cls):
        return cls.num_empleados

print("=== MÉTODOS ESTÁTICOS Y DE CLASE ===")
print("¿17 es primo?", MathUtils.es_primo(17))
emp1 = Empleado("Ana", 3000)
emp2 = Empleado.desde_salario_anual("Carlos", 48000)
print("Total empleados:", Empleado.total_empleados())