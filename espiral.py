def generar_espiral(dimensiones):
    espiral = [[0] * dimensiones for _ in range(dimensiones)]

    indicaciones = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    fila, columna = dimensiones // 2, dimensiones // 2
    espiral[fila][columna] = 1

    numero = 2
    dimension_actual = 1
    indicacion_actual = 1

    while dimension_actual < dimensiones:
        for _ in range(2):
            for _ in range(dimension_actual):
                columna += indicaciones[indicacion_actual][0]
                fila += indicaciones[indicacion_actual][1]
                espiral[fila][columna] = numero
                numero += 1

            indicacion_actual = (indicacion_actual + 1) % 4
            dimension_actual += 1

    return espiral

def suma_diagonales(espiral):
    suma = 0
    dimensiones = len(espiral)
    diag_principal = [espiral[i][i] for i in range(dimensiones)]
    diag_secundaria = [espiral[i][dimensiones - 1 - i] for i in range(dimensiones)]
    numero_principal = espiral[dimensiones // 2][dimensiones // 2]
    suma = sum(diag_principal) + sum(diag_secundaria) - numero_principal

    return suma

diag_espiral = 1001
mostrar_espiral = generar_espiral(diag_espiral)
respuesta = suma_diagonales(mostrar_espiral)

print(f"La suma de las diagonales de {diag_espiral}x{diag_espiral} es: {respuesta}")




