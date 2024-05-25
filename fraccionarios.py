def potencias():
    potencia = 1
    fraccion = 0.5
    suma = 0.5

    print("Potencia  fraccion  suma")

    while fraccion > 0.000001:
        print(f"{potencia}\t{fraccion}\t{suma}")
        potencia +=1
        fraccion /= 2
        suma += fraccion
potencias()