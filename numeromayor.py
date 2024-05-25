def numero_mayor(numeros):
    mayor = sorted(numeros, reverse=True)[0] #la lista se ordene de mayor a menor
    return mayor

n = int(input("ingresa la cantidad de numeros: "))
usuario= [float(input(f"ingresa el numero{i + 1}: "))for i in range(n)]
hallar_mayor = numero_mayor(usuario)
print(f"El numero mayor de los ingresados es {hallar_mayor}")
