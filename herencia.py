class Persona():
    def __init__(self, apeMat, apePat, nom):
        self.apellidoPaterno = apePat
        self.apellidoMaterno = apeMat
        self.nombre = nom
    
class Estudiante(Persona):



#aca estamos indicando que la classe llamada Estudiante, va a HEREDAR todo lo que tenga la clase persona, esto se usa para reutilizar codigo
#ya que puede pasar que muchas classes tengas cosas en comun, es decir, un estudiante y una persona tienen apellido materno, paterno y nombre
#entonces para no repetir lo que ya pusimos, lo hacemos heredar, tambien podemos hacer que herede y agregarle datos

