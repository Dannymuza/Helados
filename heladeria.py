# Lista de helados
helados = []

# Menú de opciones
print("Gestión de Helados")
print("1. Agregar helado")
print("2. Mostrar lista de helados")
print("3. Modificar helado")
print("4. Eliminar helado")
print("5. Salir")

opcion = 0

while opcion != 5:
    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:  # Agregar helado
        print("Agregando un nuevo helado")
        nombre = input("Nombre del helado: ")
        descripcion = input("Descripción: ")
        precio = input("Precio: ")

        if precio.replace(".", "", 1).isdigit():
            precio = float(precio)
            helado = {
                "id": len(helados) + 1,  # Asignar ID único
                "nombre": nombre,
                "descripcion": descripcion,
                "precio": precio
            }
            helados.append(helado)
            print(f"Helado '{nombre}' agregado exitosamente.")
        else:
            print("Error: El precio debe ser un número.")

    elif opcion == 2:  # Mostrar lista de helados
        print("Lista de Helados:")
        if helados:
            for h in helados:
                print(f"ID: {h['id']} | Nombre: {h['nombre']} | Descripción: {h['descripcion']} | Precio: ${h['precio']:.2f}")
        else:
            print("No hay helados registrados.")

    elif opcion == 3:  # Modificar helado
        id_modificar = input("Ingrese el ID del helado a modificar: ")

        if id_modificar.isdigit():
            id_modificar = int(id_modificar)
            helado_encontrado = None

            for h in helados:
                if h["id"] == id_modificar:
                    helado_encontrado = h
                    break

            if helado_encontrado:
                print(f"Modificando el helado '{helado_encontrado['nombre']}'")

                nuevo_nombre = input(f"Nuevo nombre ({helado_encontrado['nombre']}): ")
                if nuevo_nombre:
                    helado_encontrado["nombre"] = nuevo_nombre

                nueva_descripcion = input(f"Nueva descripción ({helado_encontrado['descripcion']}): ")
                if nueva_descripcion:
                    helado_encontrado["descripcion"] = nueva_descripcion

                nuevo_precio = input(f"Nuevo precio (${helado_encontrado['precio']:.2f}): ")
                if nuevo_precio.replace(".", "", 1).isdigit():
                    helado_encontrado["precio"] = float(nuevo_precio)
                    print("Helado modificado exitosamente.")
                elif nuevo_precio:
                    print("Error: El precio debe ser un número.")
            else:
                print("No se encontró un helado con ese ID.")
        else:
            print("Error: Ingrese un número válido.")

    elif opcion == 4:  # Eliminar helado
        id_eliminar = input("Ingrese el ID del helado a eliminar: ")

        if id_eliminar.isdigit():
            id_eliminar = int(id_eliminar)
            helado_encontrado = None

            for h in helados:
                if h["id"] == id_eliminar:
                    helado_encontrado = h
                    break

            if helado_encontrado:
                helados.remove(helado_encontrado)
                print(f"Helado '{helado_encontrado['nombre']}' eliminado.")
            else:
                print("No se encontró un helado con ese ID.")
        else:
            print("Error: Ingrese un número válido.")

    elif opcion == 5:  # Salir
        print("Saliendo del programa... Hasta pronto!")

    else:
        print("Opción inválida. Intente nuevamente.")