import uuid


helados = [] 

def generar_id():
    
    return str(uuid.uuid4())[:8]  

def crear_helado():
    
    nombre = input("Ingrese el nombre del helado: ")
    descripcion = input("Ingrese la descripción del helado: ")
    precio = float(input("Ingrese el precio del helado: "))
    
    helado = {
        "id": generar_id(),
        "nombre": nombre,
        "descripcion": descripcion,
        "precio": precio
    }
    helados.append(helado)
    print("\nHelado agregado exitosamente!\n")

def ver_helados():
    
    if not helados:
        print("No hay helados registrados.\n")
        return
    
    print("\nLista de helados:")
    for h in helados:
        print(f"ID: {h['id']} | Nombre: {h['nombre']} | Descripción: {h['descripcion']} | Precio: ${h['precio']:.2f}")
    print()

def modificar_helado():
    
    ver_helados()
    id_buscar = input("Ingrese el ID del helado a modificar: ")
    for h in helados:
        if h['id'] == id_buscar:
            h['nombre'] = input(f"Nuevo nombre ({h['nombre']}): ") or h['nombre']
            h['descripcion'] = input(f"Nueva descripción ({h['descripcion']}): ") or h['descripcion']
            h['precio'] = float(input(f"Nuevo precio (${h['precio']}): ") or h['precio'])
            print("\nHelado actualizado con éxito!\n")
            return
    print("\nID no encontrado.\n")

def eliminar_helado():
    
    ver_helados()
    id_buscar = input("Ingrese el ID del helado a eliminar: ")
    for i, h in enumerate(helados):
        if h['id'] == id_buscar:
            del helados[i]
            print("\nHelado eliminado con éxito!\n")
            return
    print("\nID no encontrado.\n")

def menu():
    
    while True:
        print("\nGestión de Helados")
        print("1. Agregar helado")
        print("2. Ver lista de helados")
        print("3. Modificar helado")
        print("4. Eliminar helado")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            crear_helado()
        elif opcion == "2":
            ver_helados()
        elif opcion == "3":
            modificar_helado()
        elif opcion == "4":
            eliminar_helado()
        elif opcion == "5":
            print("\nSaliendo del programa...\n")
            break
        else:
            print("\nOpción no válida. Intente nuevamente.\n")

if __name__ == "__main__":
    menu()
