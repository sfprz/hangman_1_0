from palabras import lista_palabras
from dibujo import etapas
import random

# Confirmaciones
abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letras_usadas = []
vidas = 6

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
        print("Ya ha utilizado la letra")
        continue
    letras_usadas.append(letra)
    break

if letra in palabra_secreta:
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            palabra_oculta[i] = letra
    print("¡Correcto! La letra está en la palabra.")
    print("Palabra oculta:", " ".join(palabra_oculta))
else:
    vidas -= 1
    print("¡Incorrecto! La letra no está en la palabra. Te quedan", vidas, "vidas.")


