class Persona:
    def __init__(self, nombre, **kwargs):
        self.nombre = nombre
        self.otros_datos = kwargs
        # kwargs serían elementos restantes llamado "otros_datos"
        # Que en este caso sería "edad" y "profesión"
p = Persona(nombre="Sergio", edad="26", profesión= "programador")
print("nombre: ",p.nombre)
print("kwargs: ",p.otros_datos) 

# Aprender sobre las clases!!! Urgente
class voleybol:
    def __init__(self,**kwargss):
        self.otros_datos = kwargss

    def ladrar(self):
        print(f"{self.otros_datos} hace guf guf")
    
A = voleybol(nombre="rex")
A.ladrar()