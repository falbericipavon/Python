# Array (lista: el primer elemento esta en la posicion 0)
tablero = ["-","-","-",
    "-","-","-",
    "-","-","-"]

# variable boolean
seguir_jugando = True

# variable
jugador_activo = "X"
ganador = None


# funcion jugar
def jugar():
  mostrar_tablero() 
  while seguir_jugando:
    manejar_turno()
    verificar_ganador()
    verificar_empate()
    cambiar_jugador()
  if ganador == "X" or ganador =="O":
    print("Ganador: " + ganador)
    print(" Felicidades ")
  else:
    print("Empate! ")

# funcion verificar_empate
def verificar_empate():
 global seguir_jugando
 if "-" not in tablero:
   seguir_jugando = False

# funcion verificar_ganador
def verificar_ganador():
  verificar_fila()
  verificar_columna()
  verificar_diagonal()

# funcion verificar_fila
def verificar_fila():
  global seguir_jugando, ganador
  fila_1 = tablero[0]==tablero[1]==tablero[2]!= "-"
  fila_2 = tablero[3]==tablero[4]==tablero[5]!= "-"
  fila_3 = tablero[6]==tablero[7]==tablero[8]!= "-"
  if fila_1 or fila_2 or fila_3:
    seguir_jugando = False
    ganador = jugador_activo

# funcion verificar_columna
def verificar_columna():
  global seguir_jugando, ganador
  col_1 = tablero[0]==tablero[3]==tablero[6]!= "-"
  col_2 = tablero[1]==tablero[4]==tablero[7]!= "-"
  col_3 = tablero[2]==tablero[5]==tablero[8]!= "-"
  if col_1 or col_2 or col_3:
    seguir_jugando = False
    ganador = jugador_activo
  
# funcion verificar_diagonal
def verificar_diagonal():
  global seguir_jugando, ganador
  dia_1 = tablero[0]==tablero[4]==tablero[8]!= "-"
  dia_2 = tablero[2]==tablero[4]==tablero[6]!= "-"
  if dia_1 or dia_2:
    seguir_jugando = False
    ganador= jugador_activo  

# funcion manejar_turno
def manejar_turno():
  global tablero, jugador_activo
  print("Turno de: " + jugador_activo)
  print("")
  posicion = ""
  valido = False
  while not valido:
    while posicion not in ["1","2","3","4","5","6","7","8","9"]:
      posicion = input ("Elegi posicion del 1 al 9: ")
    posicion = int(posicion) -1
    if tablero[posicion] == "-":
      valido = True
    else:
      print("Esta posicion ocupada")
      print("")
  
  tablero[posicion] = jugador_activo
  mostrar_tablero()

# funcion cambiar_jugador
def cambiar_jugador():
  global jugador_activo
  if jugador_activo == "X":
    jugador_activo = "O"
  else:
   jugador_activo = "X"

def jugarDeNuevo():
    # Esta función devuelve True si el jugador quiere volver a jugar, en caso contrario devuelve False.
    print()
    print('¿Quieres jugar de nuevo? (sí o no)')
    return input().lower().startswith('s')

# funcion tablero
def mostrar_tablero():
  print("")
  print("TA TE TI")
  print(tablero[0] + " | " + tablero[1] + " | " + tablero[2])
  print(tablero[3] + " | " + tablero[4] + " | " + tablero[5])
  print(tablero[6] + " | " + tablero[7] + " | " + tablero[8])
  print("")


# Mostrar en pantalla
jugar() 