import random

AHORCADO = [
    '''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    ========='''
]
words = 'ABEJA ARDILLA AVESTRUZ ALCE CISNE BURRO BOA BUFALO CUERVO CIERVO CABRA CEBRA CABALLO CERDO COBRA DELFIN DROMEDARIO FOCA FLAMENCO GATO GORILA GALLINA GANZO HURON HIPOPOTAMO HAMSTER IGUANA JIRAFA JAGUAR JABALI KOALA LEON LINCE LOBO LAGARTO LORO MONO MAMUT MULA MARMOTA NUTRIA OVEJA OSO ORCA PERRO PATO PANDA RANA RATON SERPIENTE SAPO TORO TOPO TORTUGA URRACA VIVORA VACA ZORRO'.split(
)


def obtenerPalabraAlAzar(listaDePalabras):
# Esta función devuelve una cadena al azar de la lista de cadenas pasada como argumento.
	indiceDePalabras = random.randint(0, len(listaDePalabras) - 1)
	return listaDePalabras[indiceDePalabras]


def mostrarTablero(AHORCADO, letrasIncorrectas, letrasCorrectas,
                   palabraSecreta):
	print(AHORCADO[len(letrasIncorrectas)])
	print()

	print('Letras incorrectas:', end=' ')
	for letra in letrasIncorrectas:
		print(letra, end=' -  ')
	print()

	espaciosVacíos = '_' * len(palabraSecreta)

	for i in range(
	    len(palabraSecreta
	        )):  # completar los espacios vacíos con las letras adivinadas
		if palabraSecreta[i] in letrasCorrectas:
			espaciosVacíos = espaciosVacíos[:i] + palabraSecreta[
			    i] + espaciosVacíos[i + 1:]

	for letra in espaciosVacíos:  # mostrar la palabra secreta con espacios entre cada letra
		print(letra, end=' ')
	print()


def obtenerIntento(letrasProbadas):
	# Devuelve la letra ingresada por el jugador. Verifica que el jugador ha ingresado sólo una letra, y no otra cosa.
	while True:
		print()
		print('Coloca una letra y adivina el animal.')
		intento = input()
		intento = intento.upper()
		if len(intento) != 1:
			print()
			print('Por favor, introduce una letra.')
		elif intento in letrasProbadas:
			print()
			print('Ya has probado esa letra. Elige otra.')
		elif intento not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
			print()
			print('Por favor ingresa una LETRA.')
		else:
			return intento


def jugarDeNuevo():
	# Esta función devuelve True si el jugador quiere volver a jugar, en caso contrario devuelve False.
	print()
	print('¿Quieres jugar de nuevo? (sí o no)')
	return input().lower().startswith('s')


print('A H O R C A D O')
letrasIncorrectas = ''
letrasCorrectas = ''
palabraSecreta = obtenerPalabraAlAzar(words)
juegoTerminado = False

while True:
	mostrarTablero(AHORCADO, letrasIncorrectas, letrasCorrectas,
	               palabraSecreta)

	# Permite al jugador escribir una letra.
	intento = obtenerIntento(letrasIncorrectas + letrasCorrectas)

	if intento in palabraSecreta:
		letrasCorrectas = letrasCorrectas + intento

		# Verifica si el jugador ha ganado.
		encontradoTodasLasLetras = True
		for i in range(len(palabraSecreta)):
			if palabraSecreta[i] not in letrasCorrectas:
				encontradoTodasLasLetras = False
				break
		if encontradoTodasLasLetras:
			print()
			print('¡GANASTE! ¡La palabra secreta es " ' + palabraSecreta +
			      ' "! ¡Excelente!')
			juegoTerminado = True
	else:
		letrasIncorrectas = letrasIncorrectas + intento

		# Comprobar si el jugador ha agotado sus intentos y ha perdido.
		if len(letrasIncorrectas) == len(AHORCADO) - 1:
			mostrarTablero(AHORCADO, letrasIncorrectas, letrasCorrectas,
			               palabraSecreta)
			print()
			print('¡PERDISTE! ¡Te has quedado sin intentos! \nDespués de ' +
			      str(len(letrasIncorrectas)) + ' intentos fallidos y ' +
			      str(len(letrasCorrectas)) +
			      ' aciertos, la palabra CORRECTA era " ' + palabraSecreta +
			      ' "')
			juegoTerminado = True

	# Preguntar al jugador si quiere volver a jugar (pero sólo si el juego ha terminado).
	if juegoTerminado:
		if jugarDeNuevo():
			letrasIncorrectas = ''
			letrasCorrectas = ''
			juegoTerminado = False
			palabraSecreta = obtenerPalabraAlAzar(words)
		else:
			print(' ')
			print('Gracias por Jugar')
			print(' ')
			break
