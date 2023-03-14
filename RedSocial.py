
class Facebook:
    def __init__(self, nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido
        
amigo1=Facebook("Pedro"," Carranza")
amigo2= Facebook("Maria"," Lopez")

class Amigo1(Facebook):
    pass  
    def verenvivo():
        return" {}{} Esta Transmitiendo en vivo el partido ".format(amigo1.nombre,amigo1.apellido)
    
class Amigo2(Facebook):
    pass
    def verPublicacion():
        return " {}{} Ha Publicado su primer post. En resposteria ".format(amigo2.nombre,amigo1.apellido)
    
notificacion1= Amigo1
notificacion2= Amigo2
print(notificacion1.verenvivo())
print(notificacion2.verPublicacion())