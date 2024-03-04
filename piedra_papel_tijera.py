import random

def funOpcionUsuario():
    options = ("Piedra", "Papel", "Tijera")
    opcionUsuario = int(input("Selecciona una opcion colocando solamente el numero: "))
    opcionUsuario -= 1
    opcionElegida = options[opcionUsuario]
    opcionComputadora = random.choice(options)
    return opcionElegida, opcionComputadora


def ganadorJuego(opcionUsuario, opcionComputadora):
    if opcionUsuario == opcionComputadora:
        print("Empate! Los dos eligieron la misma opción.")
        return "empate"
    
    match opcionUsuario:
        case "Piedra":
            if opcionComputadora == "Papel":
                print("Perdiste! El Papel le gana a la Piedra.")
                return "perdiste"
            elif opcionComputadora == "Tijera":
                print("Ganaste! La Piedra le gana a la Tijera.")
                return "ganaste"
        case "Papel":
            if opcionComputadora == "Tijera":
                print("Perdiste! La Tijera le gana al Papel.")
                return "perdiste"
            elif opcionComputadora == "Piedra":
                print("Ganaste! El Papel le gana a la Piedra.")
                return "ganaste"
        case "Tijera":
            if opcionComputadora == "Piedra":
                print("Perdiste! La Piedra le gana a la Tijera.")
                return "perdiste"
            elif opcionComputadora == "Papel":
                print("Ganaste! La Tijera le gana al Papel.")
                return "ganaste"


def jugar():
    ronda = 1
    computadoraScore = 0
    usuarioScore = 0
    empatesObtenidos = 0
    seguirJugando = True

    print("Bienvenido al Juego de Piedra, Papel o Tijera")

    while seguirJugando == True:
        print("Ronda: " + str(ronda) + ". Tu Puntaje: " + str(usuarioScore) + ". Puntaje de la computadora: " + str(computadoraScore))
        print(" ")
        print("En cada ronda podras elegir entre una de estas opciones: 1 Piedra, 2 Papel y 3 Piedra")

        opcionUsuario, opcionComputadora = funOpcionUsuario()
            
        print("Seleccionaste: " + str(opcionUsuario) + ". La computadora selecciono: " + str(opcionComputadora))
        print(" ")
        resultados = ganadorJuego(opcionUsuario, opcionComputadora)
        if resultados == "ganaste":
            usuarioScore += 1
        elif resultados == "perdiste":
            computadoraScore += 1
        elif resultados == "empate":
            empatesObtenidos += 1
                
        terminarJuego = input("¿Quieres jugar de nuevo? (sí o no)\n")
        if terminarJuego == "si":
            ronda += 1
            seguirJugando = True
        elif terminarJuego == "no":
            print("Gracias por Jugar. En " + str(ronda) + " rondas ganaste: " + str(usuarioScore) + " perdiste: " + str(computadoraScore) + " y empataste: " + str(empatesObtenidos))
            seguirJugando = False
        else:
            print("No elegiste una opción correcta.")
            seguirJugando = False


jugar()