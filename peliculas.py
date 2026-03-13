# 1. Generar la lista vacía
peliculas = []

# Usamos un bucle para que el programa se repita
opcion = ""

while opcion != "4":
    
    print("\n--- MENÚ DE PELÍCULAS ---")
    print("1. Agregar película")
    print("2. Borrar película")
    print("3. Ver lista")
    print("4. Salir")
    
    opcion = input("\nElige una opción: ")

    
    if opcion == "1":
     
        nombre = input("Nombre de la película: ")
        genero = input("Género: ")
        
        nueva_pelicula = {"nombre": nombre, "genero": genero}
        peliculas.append(nueva_pelicula)
        print("¡Película agregada!")

    elif opcion == "2":
        # BORRAR
        if len(peliculas) > 0:
            nombre_borrar = input("Nombre de la película a eliminar: ")
            # Buscamos la película en la lista
            for p in peliculas:
                if p["nombre"] == nombre_borrar:
                    peliculas.remove(p)
                    print("Película eliminada.")
                    break
            else:
                print("No se encontró esa película.")
        else:
            print("La lista está vacía.")

    elif opcion == "3":
        # VER
        print("\n--- TU LISTA ---")
        if not peliculas:
            print("No hay películas registradas.")
        else:
            for p in peliculas:
                print(f"- {p['nombre']} ({p['genero']})")

    elif opcion == "4":
        # SALIR
        print("Saliendo del programa... ¡Adiós!")
        
    else:
        # OTRA COSA
        print("Opción no válida. El programa se cerrará.")
        break