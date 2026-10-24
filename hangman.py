from palabras import lista_palabras
import random

## Seleccionar una palabra al azar
palabra_secreta = random.choice(lista_palabras)
palabra_oculta = ["_"] * len(palabra_secreta)

print("ingrese una letra: ")
letra = input().upper()
