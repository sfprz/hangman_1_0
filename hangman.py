from palabras import lista_palabras
import random

# Abecedario para la confirmacion
abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letras_usadas = []

# Seleccionar una palabra al azar
palabra_secreta = random.choice(lista_palabras)
palabra_oculta = ["_"] * len(palabra_secreta)

# verificaciones 

while True:
    print("ingrese una letra: ")
    letra = input().upper()

    if len(letra) != 1:
        print("Debe ingresar solo 1 letra")
        continue
    elif letra not in abecedario:
        print("Debe ingresar una letra del abecedario")
        continue
    elif letra in letras_usadas:
        print("Ya has ingresado esa letra")
        continue
    letras_usadas.append(letra)
    break



