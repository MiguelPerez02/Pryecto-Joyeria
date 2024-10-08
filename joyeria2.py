import os

# Lista de productos disponibles
productos = [
    {"nombre": "Anillo de plata", "precio": 1000, "cantidad": 12},
    {"nombre": "Anillo de oro", "precio": 6000, "cantidad": 5},
    {"nombre": "Anillo de Cuarzo", "precio": 400, "cantidad": 8},
    {"nombre": "Anillo de Diamante", "precio": 10000, "cantidad": 5}
]

# Carrito de compras
carrito = []

# Función para limpiar la pantalla
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

# Función para mostrar productos
def mostrar_productos():
    limpiar_pantalla()
    print("\n" + "="*30)
    print("-----PRODUCTOS DISPONIBLES-----")
    print("="*30)
    for i, producto in enumerate(productos):
        print(f"{i + 1}. {producto['nombre']} - ${producto['precio']:.2f} (Cantidad: {producto['cantidad']})")
    print("="*30)
    print("0. Volver al menú principal")

# Función para agregar productos al carrito
def agregar_al_carrito():
    while True:
        mostrar_productos()
        try:
            eleccion = int(input("\nSelecciona el número del producto que deseas agregar al carrito: ")) - 1
            if eleccion == -1:
                break
            if eleccion < 0 or eleccion >= len(productos):
                print("\nNúmero de producto no válido.")
                continue
            cantidad = int(input("¿Cuántas unidades deseas agregar? "))
            if cantidad <= 0:
                print("\nCantidad no válida.")
                continue
        except ValueError:
            print("\nEntrada no válida. Por favor, ingresa un número.")
            continue
        
        if productos[eleccion]["cantidad"] >= cantidad:
            productos[eleccion]["cantidad"] -= cantidad
            # Verificar si el producto ya está en el carrito
            producto_en_carrito = next((item for item in carrito if item["nombre"] == productos[eleccion]["nombre"]), None)
            if producto_en_carrito:
                producto_en_carrito["cantidad"] += cantidad
            else:
                carrito.append({"nombre": productos[eleccion]["nombre"], "precio": productos[eleccion]["precio"], "cantidad": cantidad})
            print(f"\n{cantidad} unidades de {productos[eleccion]['nombre']} agregadas al carrito.")
        else:
            print("\nNo hay suficiente stock disponible.")
        input("\nPresiona Enter para continuar...")

# Función para mostrar el carrito
def mostrar_carrito():
    limpiar_pantalla()
    while True:
        print("\n" + "="*30)
        print("   Carrito de compras")
        print("="*30)
        if carrito:
            total = 0
            for item in carrito:
                print(f"{item['nombre']} - ${item['precio']:.2f} (Cantidad: {item['cantidad']})")
                total += item["precio"] * item["cantidad"]
            print("="*30)
            print(f"Total: ${total:.2f}")
        else:
            print("El carrito está vacío.")
        print("="*30)
        print("0. Volver al menú principal")
        
        opcion = input("Selecciona una opción: ")
        if opcion == '0':
            break

# Función para calcular el total
def calcular_total():
    total = sum(item["precio"] * item["cantidad"] for item in carrito)
    print(f"\nTotal a pagar: ${total:.2f}")
    input("\nPresiona Enter para continuar...")

# Función para finalizar la compra
def finalizar_compra():
    while True:
        limpiar_pantalla()
        print("\n" + "="*30)
        print("   Finalizar compra")
        print("="*30)
        if carrito:
            total = 0
            for item in carrito:
                print(f"{item['nombre']} - ${item['precio']:.2f} (Cantidad: {item['cantidad']})")
                total += item["precio"] * item["cantidad"]
            print("="*30)
            print(f"Total: ${total:.2f}")
        else:
            print("El carrito está vacío.")
            print("="*30)
            print("0. Volver al menú principal")
            opcion = input("Selecciona una opción: ")
            if opcion == '0':
                break
            continue
        
        print("1. Volver al menú principal")
        print("2. Finalizar compra")
        
        opcion = input("Selecciona una opción: ")
        if opcion == '1':
            break
        elif opcion == '2':
            calcular_total()
            carrito.clear()
            print("\nCompra finalizada. ¡Gracias por tu compra!")
            input("\nPresiona Enter para continuar...")
            break
        else:
            print("\nOpción no válida. Intenta de nuevo.")

# Menú principal
def menu():
    while True:
        limpiar_pantalla()
        print("\n" + "="*30)
        print("---------MENU JOYERIA---------")
        print("="*30)
        print("1. Mostrar productos")
        print("2. Agregar producto al carrito")
        print("3. Mostrar carrito")
        print("4. Finalizar compra")
        print("5. Salir")
        print("="*30)
        
        try:
            opcion = int(input("Selecciona una opción: "))
        except ValueError:
            print("\nEntrada no válida. Por favor, ingresa un número.")
            continue
        
        if opcion == 1:
            mostrar_productos()
            input("\nPresiona Enter para continuar...")
        elif opcion == 2:
            agregar_al_carrito()
        elif opcion == 3:
            mostrar_carrito()
        elif opcion == 4:
            finalizar_compra()
        elif opcion == 5:
            print("\nSaliendo del programa. ¡Hasta luego!")
            break
        else:
            print("\nOpción no válida. Intenta de nuevo.")

# Función principal
def main():
    menu()

# Ejecutar el programa
if __name__ == "__main__":
    main()