#libro.py
class Libro:
    id = 0
    libros = []

    def __init__(self, titulo, categoria, fecha, autor):
        self.id = Libro.aumentar_id()
        self.titulo = titulo
        self.categoria = categoria
        self.fecha = fecha
        self.autor = autor
        Libro.agregar_libro(self)

    @classmethod
    def aumentar_id(cls):
        cls.id += 1
        return cls.id
    
    @classmethod
    def agregar_libro(cls, libro):
        cls.libros.append(libro)