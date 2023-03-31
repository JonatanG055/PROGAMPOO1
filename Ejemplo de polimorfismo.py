class VerTiktok:
    def __init__(self, nombre):
        self.nombre=nombre
tiktoker1=VerTiktok(" la tamalera")
tiktoker2= VerTiktok(" Wichito")

class Ixar(VerTiktok):
    pass  
    def verTiktok():
        return"Ver tiktok de {}".format(tiktoker1.nombre)
    
class Andrea(VerTiktok):
    pass
    def verTiktok():
        return " Ver tiktok de {}".format(tiktoker2.nombre)
    
visitante1 = Ixar 
visitante2= Andrea
print(visitante1.verTiktok())
print(visitante2.verTiktok())
          