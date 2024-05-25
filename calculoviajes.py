def tiempo_viaje():
    minutos=0

    while True:
        tiempodetramo = int (input(" ingresar los tiempos de viaje de los tramos  (ingresa 0 para terminar)"))
        if tiempodetramo ==0:
            break #si no ingresa valores sino unicamente 0
        else:
            minutos += tiempodetramo
            #entonces se hara el calculo 
    horas=minutos // 60
    min= minutos % 60
    print(f"El tiempo total de vieaje fue: {horas} hora con {min} minutos")

if __name__ == "__main__":
    tiempo_viaje()