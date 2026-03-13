""" ## diccionarios
#una estructura de datos

#que guarda datos en formato clave,valor
# clave:valor
#"nombre":"javier"

#persona ={
 #   "nombre" : "javier",
  #  "edad" : 32,
   # "direccion" : "los bravos",
    #"ciudad"  :  "rancagua"
#}

#acceder a los valores de nuestro diccionario con ["keys"]
#print(persona["ciudad"])


#modificar valores

#persona["edad"] = 35
#persona["nombre"] = "karen"


#print(persona)

#agregar un dato nuevo


#persona["pais"] ="chile"
#persona["sexo"] ="masculino"
#persona["altura"] =175


#print(persona)

#recorrer el diccionario
#iterar keys
#for i in persona:
  #  print(i)

##iterar values

#for v in persona.values():
#    print(v)

#iterar todo

#for k , v in persona.items():
  #  print(k,v)     


alumnos =[]


while True:
    print("-----menu-----")
    print("1.agregar alumno")
    print("2.ver alumnos")
    print("3. salir")


    opcion = input("elige una opcion")

    if opcion == "1":
        nombre = input("nombre de alumno")
        edad = input("edad del alumno")
        ciudad = input("de donde es")
        sexo = input("genero")

        alumno = {
            "nombre":nombre,
            "edad":edad,

        }
        alumnos.append(alumno)

        print("alumno agregado")


    elif opcion =="2":
        print("----lista de alumnos----")

        for alumno in alumnos:
            print(alumno["nombre"],"--", alumno["edad"])
    

    elif opcion == "3":
        print("programa cerrado")
        break
    else:
        print("opcion incorrecta")
 """



#proyecto de lista de peliculas netflix

 #pelicula = {
  #  nombre : nombre
  #  anio:anio
  #  actores:[actor1,actor2,...]
#}



#peliculas =lista[{pelicula1},{pelicula2}...]
#int()

#flujo del programa
"""
 generar la lista vacia
peliculas=[]
imprimir 
menu
1. agregar pelicula a la lista
2. borrar
3. ver
4. salir

que el usuario entregue la opcion

  ingresamos nombre de la pelicula
ingresamos al anio
ingresar genero
pelicula = {
    nombre : nombre
    anio:anio
    genero:genero]
    }
agregar la pelicula a la lista(append)
mesaje que la pelicula esta guardada

si el usuario eligio 2
            ingresar la pelicula a borrar
            buscamos la peliciula a borrar
            borramos
si el usuario eligio 3
            ver listado
si el usuario eligio 4 
            break   
            mensaje de salida

si el usuario puso otra cosa el programa se cierra


 """
peliculas = []

while True:
    print("\n--- MENU ---")
    print("1. Agregar película")
    print("2. Borrar película")
    print("3. Ver lista")
    print("4. Salir")

    opcion = input("\nElige una opción: ")

    if opcion == "1":
        nombre = input("Nombre de la película: ")
        anio = input("Año de la película: ")
        genero = input("Género: ")
        
        nueva_pelicula = {
            "nombre": nombre,
            "anio": anio,
            "genero": genero
        }
        peliculas.append(nueva_pelicula)
        print("¡Película agregada!")

    elif opcion == "2":
        if len(peliculas) > 0:
            nombre_borrar = input("Nombre de la película a borrar: ")
            encontrado = False
            
            for peli in peliculas:
                # Corregido: nombre_borrar debe coincidir con el input de arriba
                if peli["nombre"] == nombre_borrar:
                    peliculas.remove(peli)
                    print("Película borrada con éxito.")
                    encontrado = True
                    break
            
            if not encontrado:
                print("No se encontró esa película.")
        else:
            print("La lista está vacía.")

    elif opcion == "3":

        print("lista")
        if not peliculas:
            print("No hay películas registradas.")
        else:
            for peli in peliculas:
               
                print("Nombre: {peli['nombre']}, Año: {peli['anio']}, Género: {peli['genero']}")

    eli4
    f opcion == "4":
        print("Saliendo del programa... ¡Adiós!")
        break 
        
    else:print("Opción no válida. El programa se cerrará.")
        break