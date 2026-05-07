# =============================================
# MÉTODOS PRIVADOS Y PROTEGIDOS
# =============================================

class Autenticador:
    def __init__(self, usuario, contraseña):
        self._usuario = usuario
        self._hash = self.__generar_hash(contraseña)

    def __generar_hash(self, contraseña):
        import hashlib
        return hashlib.sha256(contraseña.encode()).hexdigest()

    def verificar(self, contraseña):
        return self.__generar_hash(contraseña) == self._hash

auth = Autenticador("admin", "1234")
print("=== MÉTODOS PRIVADOS ===")
print("Verificar correcta:", auth.verificar("1234"))
print("Verificar incorrecta:", auth.verificar("wrong"))
# print(auth.__generar_hash("test"))  # AttributeError
print()

# Métodos protegidos para herencia
class Forma:
    def calcular_area(self):
        return self._obtener_area()

    def _obtener_area(self):
        raise NotImplementedError("Implementar en subclase")

class Circulo(Forma):
    def __init__(self, radio):
        self._radio = radio
    def _obtener_area(self):
        return 3.1416 * self._radio ** 2

c = Circulo(5)
print("Área desde método protegido:", c.calcular_area())
print()

# Validación con métodos privados (Formulario)
class Formulario:
    def __init__(self):
        self._errores = {}

    def validar(self, datos):
        self._errores = {}
        self.__validar_campos_requeridos(datos)
        self.__validar_email(datos)
        return len(self._errores) == 0

    def __validar_campos_requeridos(self, datos):
        if "nombre" not in datos or not datos["nombre"]:
            self._errores["nombre"] = "Nombre obligatorio"

    def __validar_email(self, datos):
        if "email" in datos and "@" not in datos["email"]:
            self._errores["email"] = "Email inválido"

    def obtener_errores(self):
        return self._errores

f = Formulario()
datos = {"nombre": "", "email": "test"}
print("¿Validación exitosa?", f.validar(datos))
print("Errores:", f.obtener_errores())