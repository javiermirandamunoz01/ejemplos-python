#print("hola mundo cruel!!!!")
"""
# VARIABLES
nombre = "javier"
edad = 32
altura = 1.75
es_profesor = True
ciudad = "rancagua"


#TIPOS DE DATOS
str #esto es un texto
int #esto es un entero
float #esto es un flotante 
bool #esto es verdadero  o falso

#INPUT
#input()


#numero = int(input("escribe un numero : "))
#resultado = numero + 1
#print(resultado)
#

#INPUT
""" precio = input("escribe un precio : ")# pedir por consola un dato tipo str
precio = int(precio) #convertir a entero el str con int(precio)
resultado = precio + 10 #el precio sumado + 10 ya que ahora es numero entero
print(resultado)# imprimeme el precio en pantalla """

## CONDICIONALES


#if condicion:
#    codigo
#comparadores
""" 
== igual
!= diferente
> mayor
< menor
>= mayor o igual
<= menor o igual 
"""


""" edad = 20

if edad >= 18:
    print("puede entrar a la disco")
elif edad >= 50:
    print("demaciado antiguo!!")
else:
    print("no puede entrar a la disco")     """


#BUCLES

#WHILE
#while condicion:
#    codigo
# while significa mientras pase algo
contador = 0

while contador < 10:
    print(contador)
    contador += 1

""" while True:
    texto = input("escribe para salir de bucle")

    if texto == "salir":
        break """


#FOR

#for elemento in lista
#    codigo

lista = ["hola","a","todos"]

for i in lista:
    print(i)






##tipos de datos 2

##listas
listas=[]  ##corchetes son importantes
##
diccionario ={"key":"value"}
##sets
sets={1,2,3,4,5,6}
##tuplas
tuplas =(1,2,3,4,5)



## listas 
##index
frutas=["pera","manzana","melon","durazno", [1,2,3,4,[5,6,7]]]
 #index    0     1      2       3     = posicion

frutas[2] = "kiwi"       # "melon" pasa a ser "kiwi"
frutas[0] = "arandano"


print(frutas[2])
print(frutas[3])
print(frutas[0])
print(frutas[4][4][0])


print(frutas[-3])

print(frutas[1])
print(frutas[0])


#append
frutas.append("naranja") #agrega un item al final de la lista

##remove
frutas.remove("manzana")


personas =["julieta","karen","renato"]

for i in personas:
    print(i)


    alumnos = [] #lista  vacia

    while True:
        print(opcion1)
        print(opcion2)
        print(opcion3)
        print(opcion4)
        print(opcion5)

        opcion = input("ingresa la opcion :")

    if opcion == "1":
        nombre = input("ingresa el nombre alumno")
        alumnos.append(nombre)
        print(alumnos)
    elif opcion == "2":
        nombre = input("ingresa el nombre alumno")
        alumnos.remove(nombre)
        print(alumnos)
    else:
          break """"""


alumnos=["karen","javier"]

print(alumnos)

len()