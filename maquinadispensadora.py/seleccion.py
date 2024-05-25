opc = int(input("\n\tSeleccione el producto que desea adquirir.\n"))
plata = 0
nombre = list(producto)[opc-1]
precio = producto.get(nombre)

def seleccionar_producto(producto):
    selection = int(input("\n\tSeleccione el producto que desea adquirir.\n"))
    nombre_producto = list(producto)[selection - 1]
    precio_producto = producto.get(nombre_producto)
    print(f"El artículo {nombre_producto} se encuentra valorado en ${precio_producto}")
    return nombre_producto, precio_producto