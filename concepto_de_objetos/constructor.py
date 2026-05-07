# =============================================
# CONSTRUCTOR __init__ Y CREACIÓN DE OBJETOS
# =============================================

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

# Crear objetos
ana = Persona("Ana García", 28)
juan = Persona("Juan López", 35)

print("=== CONSTRUCTOR ===")
print(ana.nombre, ana.edad)
print(juan.nombre, juan.edad)
print()

# Valores predeterminados
class Producto:
    def __init__(self, nombre, precio, stock=0):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

laptop = Producto("Laptop XPS", 1200)
teclado = Producto("Teclado mecánico", 80, 15)
print("Stock laptop:", laptop.stock)
print("Stock teclado:", teclado.stock)
print()

# Inicialización con cálculos
class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        self.area = ancho * alto
        self.perimetro = 2 * (ancho + alto)

rect = Rectangulo(5, 3)
print("Rectángulo - área:", rect.area, "perímetro:", rect.perimetro)
print()

# Validación en constructor
class Cuenta:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        if saldo_inicial < 0:
            raise ValueError("El saldo inicial no puede ser negativo")
        self.saldo = saldo_inicial

cuenta_ana = Cuenta("Ana García", 1000)
print("Cuenta creada:", cuenta_ana.titular, cuenta_ana.saldo)
print()

# Constructores alternativos con @classmethod
class Fecha:
    def __init__(self, dia, mes, año):
        self.dia = dia
        self.mes = mes
        self.año = año

    @classmethod
    def desde_texto(cls, texto):
        dia, mes, año = map(int, texto.split('-'))
        return cls(dia, mes, año)

    @classmethod
    def hoy(cls):
        import datetime
        f = datetime.date.today()
        return cls(f.day, f.month, f.year)

fecha1 = Fecha(15, 3, 2023)
fecha2 = Fecha.desde_texto("25-12-2023")
fecha3 = Fecha.hoy()
print("Fechas:", f"{fecha1.dia}/{fecha1.mes}/{fecha1.año}",
      f"{fecha2.dia}/{fecha2.mes}/{fecha2.año}",
      f"{fecha3.dia}/{fecha3.mes}/{fecha3.año}")