
class Entretenimiento:
    def __init__(self, nombre,duracion):
        self.nombre=nombre
        self.duracion=duracion
ir1=Entretenimiento("Rapido y furioso",160)
ir2=Entretenimiento("Cien años de soledad",789)
ir3=Entretenimiento("The Legen of Zelda : Breath of the wild ",200)
class Pelicula(Entretenimiento):
    pass  
    def optener_informacion():   
        personaje="Dominic Dom Toretto "
        return"la pelicula {} dura {} minutos personaje de la pelicula {}".format(ir1.nombre,ir1.duracion, personaje)
class Libro(Entretenimiento):
    pass
    def optener_informacion():
        Autor= " Gabriel Garcia Marquez"
        return"Libro  {} dura {} Minutos Escrito por {} ".format(ir2.nombre,ir2.duracion, Autor)
class Videojuegos(Entretenimiento):
    pass
    def optener_informacion():    
        Plataforma= " Nintendo Swich"
        return"{} dura {} minutos Para la Plataforma {}".format(ir3.nombre,ir3.duracion,Plataforma)
verInf=Pelicula
verInf1=Libro
verInf2=Videojuegos

print(verInf.optener_informacion())
print(verInf1.optener_informacion())
print(verInf2.optener_informacion())
