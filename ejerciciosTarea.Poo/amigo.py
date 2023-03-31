class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
class Amigo(Persona):
    def __init__(self, nombre, edad, cercano):
        super().__init__(nombre, edad)
        self.cercano = cercano
persona1 = Persona("Juan", 25)
amigo1 = Amigo("María", 30, True)
amigo2 = Amigo("Pedro", 28, False)
def presentar_persona(persona):
    print(f"Hola, mi nombre es {persona.nombre} y tengo {persona.edad} años.")

def presentar_amigo(amigo):
    tipo = "cercano" if amigo.cercano else "conocido"
    print(f"Hola, soy {amigo.nombre} y soy un amigo {tipo}.")

# Ejemplo de uso:
presentar_persona(persona1)  # Hola, mi nombre es Juan y tengo 25 años.
presentar_amigo(amigo1)  # Hola, soy María y soy un amigo cercano.
presentar_amigo(amigo2)  # Hola, soy Pedro y soy un amigo conocido.
