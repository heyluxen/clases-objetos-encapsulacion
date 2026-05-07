# =====================
# GETTERS Y SETTERS
# =====================

class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    # Getter y setter para nombre
    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nuevo_nombre):
        if isinstance(nuevo_nombre, str) and len(nuevo_nombre) > 0:
            self._nombre = nuevo_nombre
        else:
            raise ValueError("Nombre no válido")

    # Getter y setter para edad
    def get_edad(self):
        return self._edad

    def set_edad(self, nueva_edad):
        if isinstance(nueva_edad, int) and 0 <= nueva_edad <= 120:
            self._edad = nueva_edad
        else:
            raise ValueError("Edad entre 0 y 120")

print("=== GETTERS Y SETTERS ===")
ana = Persona("Ana López", 29)
print(ana.get_nombre(), ana.get_edad())
ana.set_nombre("Ana María")
ana.set_edad(30)
print(ana.get_nombre(), ana.get_edad())
try:
    ana.set_edad(-5)
except ValueError as e:
    print("Error:", e)
print()

# Ejemplo práctico con Producto
class Producto:
    def __init__(self, nombre, precio, stock=0):
        self._nombre = nombre
        self._precio = precio
        self._stock = stock
        self._descuento = 0

    def get_precio(self):
        return self._precio * (1 - self._descuento)

    def set_precio(self, nuevo_precio):
        if nuevo_precio < 0:
            raise ValueError("Precio no negativo")
        self._precio = nuevo_precio

    def set_descuento(self, desc):
        if 0 <= desc <= 1:
            self._descuento = desc

prod = Producto("Laptop", 1000, 10)
prod.set_descuento(0.15)
print("Precio con descuento:", prod.get_precio())