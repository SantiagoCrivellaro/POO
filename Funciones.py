# def nombre_funcion():   
#     pass

# nombre_funcion()
#lo que hace el pass es que no haga nada que pase.

# def saludar(nombre):
#     print("hola", nombre)
    
# saludar("Santiago")
#el string "santiago" define el argumento nombre, que se guarda en el print.

# def saludar(nombre):
#     print("hola", nombre)
    
# llamada = saludar("Santiago")
# print(llamada)
#nos devuelve none, por que saludar() ejecuta todo el codidog, asi que nos pasa "Hola santiago" pero una ves que lo pasa, se convierte en None
#entonces una ves que lo pasa, llamada = none, y abajo estamos llamandola.


# def media(num_1,num_2,num_3,num_4):
#     resultado = num_1 + num_2 + num_3 + num_4
#     resultado = resultado/4
#     return resultado

# llamada = media(5,6,7,2)
# print(llamada)

"""le dimos valores a los argumentos, se sumaron, se divieron, y con el return se devolvieron
todo eso se convirtio en la media, que lo guardamos en la variable llamada y luego la mostramos"""
#return va acompañado de un valor, asi q podiamos haber hecho todo en 1 linea

# def media(num_1,num_2,num_3,num_4):
#     return(num_1 + num_2 + num_3 + num_4)/3

# llamada = media(2,12,56,8)
# print(llamada)
#una ves se sume y divida todo el return hara la devolucion


#Diferencias Print vs Return

#print es una funcion de python para imprimir valores en consola y visualizarlos
#return se usa para devoler el resultado, por eso antes nos dio None, pq pusimos print, con return se nos ejecutaria el resultado
# y luego con print lo mostramos

#el return tambien corta el codigo

# def imprime_cosas():
#     print("hola")
#     return
#     print("Chau")
# #el 2do print no se ejecuta

#el orden de los argumentos importa.

# def resta(num_1, num_2):
#     return num_1 - num_2

# print(resta(3, 5))
# print(resta(5, 3))
# -2, 2

# print(resta(num_1= 5, num_2= 3))
#eso es pq yo asigne q valor queria, para evitar fallos en los ordenes 

def suma(num_1= 5, num_2= 5):
    return num_1 + num_2 

print(suma())
#no hace falta darle un valor a los numeros pq ya se los dimos

def resta(num_1 = 3, num_2 = 2):
    return num_1 - num_2

#print("con valores por defecto:") , resta()) = 1
#print("usando el orden con 1 solo valor:") , resta(5)) = 3
#print("usando el orden con todos los valores:") , resta(5 , 3)) = 2
#print("con keywords arguments:") resta(num_1 = 5 , num_2 = 3) = 2
#print("con un solo keyword argument:") resta(num_2 = 3)) = 0
