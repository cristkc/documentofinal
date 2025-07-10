Productos = {
    "8475HD": ["HP", 15.6, "8GB", "DD", "1T", "Intel Core i5", "Nvidia GTX1050"],
    "2175HD": ["lenovo", 14, "4GB", "SSD", "512GB", "intel Core i5", "Nvidia GTX1050"],
    "jjfFHD": ["Asus", 14, "16GB", "SSD", "256GB", "Intel core i7", "Nvidia RTX2080Ti"],
    "fgdxFHD": ["HP", 15.6, "8GB", "DD", "1T", "Intel core i3", "integrada"],
    "GF75HD": ["Asus", 15.6, "8GB", "DD", "1T", "Intel core i7", "Nvidia GTX1050"],
    "123FHD": ["lenovo", 14, "6GB", "DD", "1T", "AMD Ryzen 5", "integrada"],
    "342FHD": ["lenovo", 15.6, "8GB", "DD", "1T", "AMD Ryzen 7", "Nvidia GTX1050"],
    "UWU131HD": ["Dell", 15.6, "8GB", "DD", "1T", "AMD Ryzen 3", "Nvidia GTX1050"],
}

stock = {
    "8475HD": [387990, 10],
    "2175HD": [327990, 4],
    "jjfFHD": [424990, 1],
    "fgdxFHD": [664990, 21],
    "123FHD": [290890, 32],
    "342FHD": [444990, 7],
    "GF75HD": [749990, 2],
    "UWU131HD": [349990, 1],
}

def Stock_marca(marca):
    total = 0
    for modelo, datos in Productos.items():
        if datos[0].lower() == marca.lower():
            cantidad = stock[modelo][1]
            total += cantidad
    print(f"Stock total de la marca {marca} es {total}")

def Buscar_por_rango_de_precios(precio_min, precio_max):
    print(f"\nModelos con precio entre ${precio_min} y ${precio_max}:")
    encontrados = False
    for modelo, (precio, _) in stock.items():
        if precio_min <= precio <= precio_max:
            marca = Productos[modelo][0]
            print(f"- {marca} - {modelo}")
            encontrados = True
    if not encontrados:
        print("No hay notebooks en ese rango de precios.")

def Actualizar_precio():
    while True:
        modelo = input("Ingrese el modelo a actualizar: ")
        if modelo in stock:
            try:
                nuevo_precio = int(input("Ingrese el nuevo precio: "))
                viejo_precio = stock[modelo][0]
                stock[modelo][0] = nuevo_precio
                print("Precio actualizado!!")
            except ValueError:
                print("Error, precio inválido.")
                continue
        else:
            print("El modelo no existe!!")
            seguir = input("¿Desea actualizar otro modelo? (s/n): ").lower()
            if seguir != "s" and seguir != "si":
                break
            else:
                continue
        seguir = input("¿Desea actualizar otro modelo? (s/n): ").lower()
        if seguir != "s" and seguir != "si":
            break


def Menu():
    op1 = 0
    while op1 != 4:
        print("""
        *** MENU PRINCIPAL ***
        1. Stock por marcas
        2. Búsqueda por precio
        3. Actualizar precio
        4. Salir
        """)
        try:
            op1 = int(input("Ingrese una opción del 1 al 4: "))
        except ValueError:
            print("Error, por favor ingrese un número válido.")
            continue

        if op1 == 1:
            marca = input("Ingrese la marca a consultar: ")
            Stock_marca(marca)
        elif op1 == 2:
            try:
                precio_minimo = int(input("Ingrese el precio mínimo: "))
                precio_maximo = int(input("Ingrese el precio máximo: "))
                Buscar_por_rango_de_precios(precio_minimo, precio_maximo)
            except ValueError:
                print("Debe ingresar valores enteros!!")
        elif op1 == 3:
            Actualizar_precio()

        elif op1 == 4:
            print("Programa finalizado")
        else:
            print("Debe seleccionar una opcion valida!!")



    
