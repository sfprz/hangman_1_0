from palabras import lista_palabras
import random

## Abecedario para la confirmacion
abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

## Seleccionar una palabra al azar
palabra_secreta = random.choice(lista_palabras)
palabra_oculta = ["_"] * len(palabra_secreta)

print("ingrese una letra: ")
letra = input().upper()

while len(letra) != 1:
    print("Debe ingresar solo 1 letra")
    print("ingrese una letra: ")
    letra = input().upper()

if letra not in abecedario:
    print("Debe ingresar una letra del abecedario")
    print("ingrese una letra: ")
    letra = input().upper()
    

