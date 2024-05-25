def cachipun(player1, player2):
    opciones_de_juego = ["piedra", "papel", "tijera"]
    if player1 == player2: 
        return "empate"
    elif (player1, player2) in [("papel", "piedra"), ("tijera", "papel"), ("piedra", "tijera")]:
        return "player1"
    else:
        return "player2"
#linea 1 a 8- son las leyes del juego 
def jugadas(numero_jugadas):
    opciones = ["piedra", "papel", "tijera"]
    while True:
        players = input(f"player{numero_jugadas}, por favor elija piedra, papel o tijera: ").lower()
        if players in opciones:
            return players
        else:
            print("¡ERROR! Por favor, elija piedra, papel o tijera.")
#si el usuario introduce algo diferente a piedra,papel o tijera el programa no funcionara.
def main():
    marcador = {"player1": 0, "player2": 0}

    while True:
        players = [jugadas(i + 1) for i in range(2)]
        resultado = cachipun(players[0], players[1])

        if resultado=="empate":
            print("Quedaron empatados en esta ronda")
        else:
            marcador[resultado] += 1
            print(f"Desenlace de la ronda: {resultado}")
            print(f"Marcador: player1 - {marcador['player1']}, player2 - {marcador['player2']}\n")

        if marcador["player1"] == 3 or marcador['player2'] == 3:
            print(f"¡El ganador de este juego es {max(marcador, key=marcador.get)}!")
            break  # Agregado para salir del bucle principal cuando se determina un ganador

if __name__ == "__main__":
    main()
