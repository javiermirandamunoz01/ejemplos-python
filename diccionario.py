## diccionarios
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












