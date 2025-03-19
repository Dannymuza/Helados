def ingresar_frutas():
   
    frutas = []
    for i in range(10):
        print(f"\nIngrese los datos de la fruta {i + 1}:")
        nombre = input("Nombre de la fruta: ")
        precio = float(input("Precio de la fruta: "))
        
        fruta = {
            "nombre": nombre,
            "precio": precio
        }
        frutas.append(fruta)
    
    return frutas

def ordenar_frutas(frutas):
    
    return sorted(frutas, key=lambda x: x['precio'], reverse=True)

def mostrar_frutas(frutas):
    
    print("\nLista de frutas ordenadas por precio (de mayor a menor):")
    for fruta in frutas:
        print(f"Nombre: {fruta['nombre']} | Precio: ${fruta['precio']:.2f}")

def main():
    
    frutas = ingresar_frutas()
    frutas_ordenadas = ordenar_frutas(frutas)
    mostrar_frutas(frutas_ordenadas)

if __name__ == "__main__":
    main()
