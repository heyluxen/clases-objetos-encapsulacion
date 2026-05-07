class Libro:
    def __init__(self, titulo, autor, paginas, disponible=True):
        """
        Constructor de la clase Libro
        
        Args:
            titulo (str): Título del libro
            autor (str): Autor del libro
            paginas (int): Número total de páginas
            disponible (bool): Estado de disponibilidad (True = disponible)
        """
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.disponible = disponible

    def prestar(self):
        """Cambia el estado a prestado si está disponible."""
        if self.disponible:
            self.disponible = False
            return f"✅ El libro '{self.titulo}' ha sido prestado."
        else:
            return f"❌ El libro '{self.titulo}' NO está disponible para préstamo."

    def devolver(self):
        """Cambia el estado a disponible si estaba prestado."""
        if not self.disponible:
            self.disponible = True
            return f"📚 El libro '{self.titulo}' ha sido devuelto."
        else:
            return f"ℹ️ El libro '{self.titulo}' ya estaba disponible en la biblioteca."

    def informacion(self):
        """Devuelve una cadena con toda la información del libro."""
        estado = "Disponible" if self.disponible else "Prestado"
        return f"📖 {self.titulo} | Autor: {self.autor} | Páginas: {self.paginas} | Estado: {estado}"

# Prueba de la clase Libro
def main():
    # Crear dos objetos libro diferentes
    libro1 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 863)
    libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", 471)

    # Mostrar información inicial de los libros
    print("=== Información inicial de los libros ===")
    print(libro1.informacion())
    print()
    print(libro2.informacion())
    print()

    # Prestar los libros
    print("=== Préstamo de libros ===")
    print(libro1.prestar())
    print(libro2.prestar())
    print()

    # Intentar prestar un libro ya prestado
    print("=== Intento de préstamo de libros ya prestados ===")
    print(libro1.prestar())
    print()

    # Mostrar información después del préstamo
    print("=== Información después del préstamo ===")
    print(libro1.informacion())
    print()

    # Devolver un libro
    print("=== Devolución de libros ===")
    print(libro1.devolver())
    print()

    # Intentar devolver un libro ya disponible
    print("=== Intento de devolución de libros ya disponibles ===")
    print(libro1.devolver())
    print()

    # Mostrar información final
    print("=== Información final de los libros ===")
    print(libro1.informacion())
    print()
    print(libro2.informacion())

if __name__ == "__main__":
    main()