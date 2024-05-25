producto = {
    "A": 270,
    "B": 340,
    "C": 390
}
listaMonedas=sorted([10, 120,50, 100, 150])

print("Catálogo de productos de la máquina dispensadora de alimentos de campusLands.\n")
cont = 0
for nombre,precio in producto.items():
    cont += 1
    print(f"\t{cont}. Producto: {nombre} --- Valor: ${precio}")
opc = int(input("\n\tSeleccione el producto que desea adquirir.\n"))
plata = 0
nombre = list(producto)[opc-1]
precio = producto.get(nombre)

print(f"El artículo {nombre} se encuentra valorado en ${precio}")

while(plata<precio):
    print("Insertar moneda")
    cont=1
    for i in listaMonedas:
        print(f"{cont}. ${i}")
        cont+=1
    moneda = int(input())
    if(moneda < cont):
        plata = plata + listaMonedas[moneda-1]
    else:
        print("Usuario, ese monto no está disponible.")
    
    print(f"El artículo {nombre} se encuentra valorado en ${precio}, mientras que su presupuesto disponible es de ${plata}.")


if plata > precio:
    plata = plata - precio
    print("Sus vueltos son: ")
    while plata != 0:
        for i in reversed(listaMonedas):
            if plata >= i:
                print("$", i)
                plata -= i

print("Gracias por su compra!")