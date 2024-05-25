def main():
    numeros_positivos = 0
    numeros_negativos = 0

    while True:
        try:
            numero = int(input("Ingrese un numero entero "))
            numero = int(input("Ingrese un numero entero "))
        except ValueError:
            print("Error: Ingrese un numero entero válido.")
            continue
            #se pide a el usuario ingresar los numeros 
        if numero == 0:
            break
        elif numero > 0:
            numeros_positivos += 1
        else:
            numeros_negativos += 1
        #ingresa los numeros el programa comprueba si son positivos o no para poder imprimirlos 
    grafico(numeros_positivos, numeros_negativos)

def grafico(numeros_positivos, numeros_negativos):
    print("Gráfico de numeroes Positivos y Negativos:")
    print("+" * numeros_positivos + " Positivos")
    print("-" * numeros_negativos + " Negativos")

if __name__ == "__main__":
    main()
