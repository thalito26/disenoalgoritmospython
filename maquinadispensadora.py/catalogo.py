def catalogo(producto):
    producto = {
    "A": 270,
    "B": 340,
    "C": 390
    }
    listaMonedas=sorted([10, 120,50, 100, 150])

    print("Catálogo de productos de la máquina dispensadora de alimentos de campusLands.\n")
    cont=0
    for nombre,precio in producto.items():
        cont += 1
    print(f"\t{cont}. Producto: {nombre} --- Valor: ${precio}")
    
    


