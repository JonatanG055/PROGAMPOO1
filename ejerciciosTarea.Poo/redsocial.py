class Persona:
    def __init__(self, nombre, edad, email):
        self.nombre = nombre
        self.edad = edad
        self.email = email
class Amigo(Persona):
    def __init__(self, nombre, edad, email, redes_sociales):
        super().__init__(nombre, edad, email)
        self.redes_sociales = redes_sociales

class MejorAmigo(Persona):
    def __init__(self, nombre, edad, email, apodo):
        super().__init__(nombre, edad, email)
        self.apodo = apodo
def mostrar_informacion(amigo):
    print(f"Nombre: {amigo.nombre}")
    print(f"Edad: {amigo.edad}")
    print(f"Email: {amigo.email}")
    if isinstance(amigo, Amigo):
        print(f"Redes sociales: {amigo.redes_sociales}")
    elif isinstance(amigo, MejorAmigo):
        print(f"Apodo: {amigo.apodo}")

amigo1 = Amigo("Juan", 25, "juan@gmail.com", ["Facebook", "Instagram"])
mostrar_informacion(amigo1)

amigo2 = MejorAmigo("Pedro", 27, "pedro@gmail.com", "Pete")
mostrar_informacion(amigo2)
