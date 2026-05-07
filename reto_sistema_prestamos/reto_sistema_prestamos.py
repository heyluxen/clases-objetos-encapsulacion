"""
Sistema de Préstamos de Equipos
Aplicación POO con clases Equipo, Usuario, Prestamo.
Encapsulación, listas, tuplas, diccionarios y menú interactivo.
"""

from datetime import datetime
from typing import List, Optional, Dict, Tuple

# ------------------------- CLASES -------------------------

class Equipo:
    """Clase que representa un equipo de cómputo."""
    def __init__(self, nombre: str):
        self.__nombre = nombre          # privado
        self.__disponible = True        # privado
        self.__historial: List[Tuple[str, str]] = []  # lista de tuplas (usuario, fecha)

    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def disponible(self) -> bool:
        return self.__disponible

    def prestar(self, usuario: str, fecha: str) -> bool:
        """Registra préstamo si está disponible. Devuelve True si éxito."""
        if not self.__disponible:
            return False
        self.__historial.append((usuario, fecha))
        self.__disponible = False
        return True

    def devolver(self) -> bool:
        """Marca como disponible si estaba prestado."""
        if self.__disponible:
            return False
        self.__disponible = True
        return True

    def obtener_historial(self) -> List[Tuple[str, str]]:
        """Devuelve copia del historial de préstamos."""
        return self.__historial.copy()

    def __str__(self) -> str:
        estado = "Disponible" if self.__disponible else "Prestado"
        return f"🔌 {self.__nombre} - {estado}"


class Usuario:
    """Clase opcional para gestionar usuarios (se puede ampliar)."""
    def __init__(self, nombre: str):
        self.__nombre = nombre

    @property
    def nombre(self) -> str:
        return self.__nombre


class Prestamo:
    """Clase opcional para registrar préstamos con más detalle."""
    pass   # No es obligatorio para el reto, pero se incluye por POO


# ------------------------- SISTEMA PRINCIPAL -------------------------

class SistemaPrestamos:
    """Gestor de equipos, préstamos y devoluciones."""
    def __init__(self):
        # Diccionario: clave = nombre del equipo, valor = objeto Equipo
        self.__equipos: Dict[str, Equipo] = {}

    def agregar_equipo(self, nombre: str) -> bool:
        """Agrega nuevo equipo si no existe."""
        nombre = nombre.strip()
        if not nombre or nombre in self.__equipos:
            return False
        self.__equipos[nombre] = Equipo(nombre)
        return True

    def mostrar_equipos(self, solo_disponibles: bool = False):
        """Muestra equipos con su estado."""
        if not self.__equipos:
            print("⚠️ No hay equipos registrados.")
            return
        for eq in self.__equipos.values():
            if solo_disponibles and not eq.disponible:
                continue
            print(eq)

    def registrar_prestamo(self, nombre_equipo: str, usuario: str) -> bool:
        """Registra préstamo si el equipo existe y está disponible."""
        nombre_equipo = nombre_equipo.strip()
        if nombre_equipo not in self.__equipos:
            print(f"❌ El equipo '{nombre_equipo}' no existe.")
            return False
        equipo = self.__equipos[nombre_equipo]
        if not equipo.disponible:
            print(f"❌ El equipo '{nombre_equipo}' ya está prestado.")
            return False
        fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if equipo.prestar(usuario, fecha_actual):
            print(f"✅ Préstamo registrado: '{nombre_equipo}' a {usuario} el {fecha_actual}")
            return True
        return False

    def devolver_equipo(self, nombre_equipo: str) -> bool:
        """Devuelve equipo si existe y estaba prestado."""
        nombre_equipo = nombre_equipo.strip()
        if nombre_equipo not in self.__equipos:
            print(f"❌ El equipo '{nombre_equipo}' no existe.")
            return False
        equipo = self.__equipos[nombre_equipo]
        if equipo.disponible:
            print(f"❌ El equipo '{nombre_equipo}' ya estaba disponible (no prestado).")
            return False
        if equipo.devolver():
            print(f"✅ Devolución registrada: '{nombre_equipo}' ahora está disponible.")
            return True
        return False

    def ver_historial(self):
        """Muestra historial completo de préstamos de todos los equipos."""
        if not self.__equipos:
            print("⚠️ No hay equipos registrados.")
            return
        for equipo in self.__equipos.values():
            print(f"\n📋 Historial de '{equipo.nombre}':")
            historial = equipo.obtener_historial()
            if not historial:
                print("   Sin préstamos registrados.")
            else:
                for usuario, fecha in historial:
                    print(f"   👤 {usuario} - {fecha}")

    def menu(self):
        """Menú interactivo principal."""
        while True:
            print("\n" + "="*50)
            print("     SISTEMA DE PRÉSTAMOS DE EQUIPOS")
            print("="*50)
            print("1. Ver todos los equipos")
            print("2. Ver equipos disponibles")
            print("3. Registrar préstamo")
            print("4. Devolver equipo")
            print("5. Ver historial de préstamos")
            print("6. Agregar nuevo equipo")
            print("7. Salir")
            opcion = input("Seleccione una opción: ").strip()

            if opcion == "1":
                print("\n--- Inventario completo ---")
                self.mostrar_equipos()
            elif opcion == "2":
                print("\n--- Equipos disponibles ---")
                self.mostrar_equipos(solo_disponibles=True)
            elif opcion == "3":
                print("\n--- Registrar préstamo ---")
                self.mostrar_equipos(solo_disponibles=True)
                equipo = input("Nombre del equipo: ")
                usuario = input("Nombre del usuario: ")
                self.registrar_prestamo(equipo, usuario)
            elif opcion == "4":
                print("\n--- Devolver equipo ---")
                equipo = input("Nombre del equipo a devolver: ")
                self.devolver_equipo(equipo)
            elif opcion == "5":
                print("\n--- Historial completo ---")
                self.ver_historial()
            elif opcion == "6":
                print("\n--- Agregar nuevo equipo ---")
                nombre = input("Nombre del equipo: ")
                if self.agregar_equipo(nombre):
                    print(f"✅ Equipo '{nombre}' agregado correctamente.")
                else:
                    print(f"❌ No se pudo agregar (nombre vacío o ya existe).")
            elif opcion == "7":
                print("👋 ¡Hasta luego!")
                break
            else:
                print("❌ Opción inválida. Intente de nuevo.")

# ------------------------- EJECUCIÓN -------------------------
if __name__ == "__main__":
    # Datos de ejemplo para mostrar funcionamiento
    sistema = SistemaPrestamos()
    sistema.agregar_equipo("Laptop Dell XPS")
    sistema.agregar_equipo("Proyector Epson")
    sistema.agregar_equipo("Tablet Samsung")
    sistema.registrar_prestamo("Laptop Dell XPS", "María García")
    sistema.menu()