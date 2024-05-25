def calcular_indice_masa_corporal(estatura, peso):
    imc = peso / (estatura ** 2)
    return imc
def evaluar_condicion_riesgo(edad, imc):
    condicion_riesgo = "Desconocida"

    if 18.5 <= imc < 24.9:
        condicion_riesgo = "Normal"
    elif 25 <= imc < 29.9:
        condicion_riesgo = "Sobrepeso"
    elif 30 <= imc < 34.9:
        condicion_riesgo = "Obesidad Clase 1"
    elif 35 <= imc < 39.9:
        condicion_riesgo = "Obesidad Clase 2"
    elif imc >= 40:
        condicion_riesgo = "Obesidad Clase 3"

    if edad >= 65 and imc >= 27:
        condicion_riesgo = "Riesgo Alto"

    return condicion_riesgo

estatura = float(input("Ingrese la estatura en metros: "))
peso = float(input("Ingrese el peso en kilogramos: "))
edad = int(input("Ingrese la edad en años: "))

imc = calcular_indice_masa_corporal(estatura, peso)


condicion_riesgo = evaluar_condicion_riesgo(edad, imc)


print(f"Su índice de masa corporal (IMC) es {imc:.2f}")
print(f"Su condición de riesgo es: {condicion_riesgo}")
