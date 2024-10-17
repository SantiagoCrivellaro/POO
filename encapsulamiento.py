"""Lo que hace el encapsulamiento es proteger atributos o metodos del exterior
y que solo se puedan modificar con operaciones predefinidas desde dentro
de la clase"""

class usuario:
    def __init__(self, nid, alias, nombre, apellido, password):
        self.nid = nid
        self.alias = alias
        self.nombre = nombre
        self.apellido = apellido
        self.__password = password
    
usuario1 = usuario("001","pde","paula","criv","saxx")

print(usuario1.password)

#con una simple llamada nos paso la contraseña, para alguien con malas intenciones seria peligroso
#lo que hacemos con el encapsulamiento es proteger el atributo, en este caso "password"
#poniendo un __ es como q no existiera, un atacante no puede verlo, pero tampoco puede cambiarlo el usuario