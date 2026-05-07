# =============================================
# ATRIBUTOS DE INSTANCIA, DE CLASE, DINÁMICOS
# =============================================

# Atributos de instancia
class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.activo = True

e1 = Estudiante("María", 20)
e2 = Estudiante("Carlos", 22)
print("=== ATRIBUTOS DE INSTANCIA ===")
print(e1.nombre, e1.edad)
print(e2.nombre, e2.edad)
print()

# Atributos de clase
class Estudiante:
    universidad = "Universidad Autónoma"  # atributo de clase

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

e1 = Estudiante("María", 20)
e2 = Estudiante("Carlos", 22)
print("=== ATRIBUTOS DE CLASE ===")
print(e1.universidad, e2.universidad, Estudiante.universidad)
Estudiante.universidad = "Universidad Complutense"
print(e1.universidad, e2.universidad)
print()

# Modificación de atributos
class Coche:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.kilometraje = 0

mi_coche = Coche("Toyota", "Corolla", "Azul")
print("=== MODIFICACIÓN ===")
print(f"Color inicial: {mi_coche.color}")
mi_coche.color = "Rojo"
mi_coche.kilometraje = 1500
print(f"Nuevo color: {mi_coche.color}, km: {mi_coche.kilometraje}")
print()

# Atributos dinámicos
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

juan = Persona("Juan")
juan.edad = 30
juan.profesion = "Ingeniero"
print("=== ATRIBUTOS DINÁMICOS ===")
print(f"{juan.nombre} tiene {juan.edad} años y es {juan.profesion}")
print()

# Atributos especiales
class Ejemplo:
    """Clase de ejemplo"""
    def __init__(self, valor):
        self.valor = valor

obj = Ejemplo(42)
print("=== ATRIBUTOS ESPECIALES ===")
print(obj.__class__)
print(Ejemplo.__name__)
print(Ejemplo.__doc__)
print(obj.__dict__)