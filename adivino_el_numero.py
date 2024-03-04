name = input("Introduce tu nombre:\n")
print("¡Hola " + name + "!")
print("")

import random

intentos_realizados = 0
numero = random.randint(1, 20)
print( name + ", estoy pensando en un número entre 1 y 20.")
print("") 

# while
while intentos_realizados < 6:
  print("Intenta adivinar.") 
  estimación = input()
  # conversion tipo de dato -> pasar de str a int
  estimación = int(estimación)
  intentos_realizados = intentos_realizados + 1
  if estimación < numero:
    print("Tu estimación es muy baja.") 
    print("") 
  if estimación > numero:
    print("Tu estimación es muy alta.")
    print("") 
  if estimación == numero:
    break

# condicional 
if estimación == numero:
  intentos_realizados = str(intentos_realizados)
  print("")
  print("¡Buen trabajo, " + name + "! ¡Has adivinado mi número en " + intentos_realizados + " intentos!")

# condicional
if estimación != numero:
  # conversion tipo de dato -> pasar de int a str
  numero = str(numero)
  print("No lo has logrado. El número que estaba pensando era " + numero)