# =============================================
# CONCEPTO TEÓRICO DE CLASE Y OBJETO
# Ejemplos: clase vacía, creación de objetos
# =============================================

class Coche:
    """Clase que representa un coche (plano)"""
    pass

# Creación de objetos (instancias)
mi_coche = Coche()
coche_de_amigo = Coche()

print("=== CLASE Y OBJETOS ===")
print(type(mi_coche))
print(isinstance(mi_coche, Coche))
print()

# Ejemplo conceptual con clase Libro
class Libro:
    """Clase que representa un libro (solo plano)"""
    pass

libro_python = Libro()
novela_fantasia = Libro()
print("Objetos Libro creados:", libro_python, novela_fantasia)