class Entretenimiento:
    def __init__(self, nombre, duracion):
        self.nombre = nombre
        self.duracion = duracion

    def obtener_info(self):
        return f"{self.nombre} ({self.duracion} minutos)"

class Pelicula(Entretenimiento):
    def __init__(self, nombre, duracion, director):
        super().__init__(nombre, duracion)
        self.director = director

    def obtener_info(self):
        return f"{self.nombre} ({self.duracion} minutos), dirigida por {self.director}"

class Libro(Entretenimiento):
    def __init__(self, nombre, duracion, autor):
        super().__init__(nombre, duracion)
        self.autor = autor

    def obtener_info(self):
        return f"{self.nombre} ({self.duracion} minutos), escrito por {self.autor}"

class Videojuego(Entretenimiento):
    def __init__(self, nombre, duracion, plataforma):
        super().__init__(nombre, duracion)
        self.plataforma = plataforma

    def obtener_info(self):
        return f"{self.nombre} ({self.duracion} minutos), para la plataforma {self.plataforma}"
pelicula = Pelicula("El Padrino", 175, "Francis Ford Coppola")
libro = Libro("Cien años de soledad", 432, "Gabriel García Márquez")
videojuego = Videojuego("The Legend of Zelda: Breath of the Wild", 200, "Nintendo Switch")

print(pelicula.obtener_info())  # El Padrino (175 minutos), dirigida por Francis Ford Coppola
print(libro.obtener_info())  # Cien años de soledad (432 minutos), escrito por Gabriel García Márquez
print(videojuego.obtener_info())  # The Legend of Zelda: Breath of the Wild (200 minutos), para la plataforma Nintendo Switch


