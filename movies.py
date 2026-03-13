# Generar la lista vacía
peliculas = []

while True:
    # Imprimir menú
    print("\n--- MENU ---")
    print("1. agregar pelicula a la lista")
    print("2. borrar")
    print("3. ver")
    print("4. salir")

    # Que el usuario entregue la opción
    opcion = input("\nElija una opción: ")

    if opcion == "1":
        # Ingresamos datos de la película
        nombre = input("ingresamos nombre de la pelicula: ")
        anio = input("ingresamos al anio: ")
        genero = input("ingresar genero: ")

        # pelicula = { nombre: nombre, anio: anio, genero: genero }
        pelicula = {
            "nombre": nombre,
            "anio": anio,
            "genero": genero
        }

       
        peliculas.append(pelicula)
        print("mensaje que la pelicula esta guardada")

    elif opcion == "2":
        
        pelicula_a_borrar = input("Ingresa el nombre de la película a borrar: ")
        
        # buscamos la pelicula a borrar
        encontrado = False
        for p in peliculas:
            if p["nombre"] == pelicula_a_borrar:
                # borramos
                peliculas.remove(p)
                print("Película eliminada con éxito.")
                encontrado = True
                break
        
        if not encontrado:
            print("No se encontró la película.")

    elif opcion == "3":
        # ver listado
        print("\n--- Listado de Películas ---")
        for p in peliculas:
            print(f"Nombre: {p['nombre']} | Año: {p['anio']} | Género: {p['genero']}")

    elif opcion == "4":
        # mensaje de salida y break
        print("Saliendo del programa... ¡Hasta luego!")
        break

    else:
        # si el usuario puso otra cosa el programa se cierra
        print("Opción no válida. Cerrando programa.")
        break
