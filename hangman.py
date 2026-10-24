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

# Verificaciones
while vidas > 0 and "_" in palabra_oculta:
    print(etapas[6 - vidas])
    print("Palabra oculta:", " ".join(palabra_oculta))

    while True:
        print("Ingrese una letra:")
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
        print("Palabra oculta:", " ".join(palabra_oculta))
        print("¡Correcto! La letra está en la palabra.")
    else:
        vidas -= 1
        print("¡Incorrecto! La letra no está en la palabra. Te quedan", vidas, "vidas.")

    if "_" not in palabra_oculta:
        print("¡Felicidades! Has adivinado la palabra:", palabra_secreta)
        break
    if vidas == 0:
        print(etapas[6])
        print("¡Has perdido! La palabra era:", palabra_secreta)
        break

while True:
    print("¿Desea jugar de nuevo? (S/N)")
    respuesta = input().upper()
    if respuesta == "S":
        palabra_secreta = random.choice(lista_palabras)
        palabra_oculta = ["_"] * len(palabra_secreta)
        letras_usadas = []
        vidas = 6
        continue
    elif respuesta == "N":
        print("¡Gracias por jugar!")
        break
    else:
        print("Debe ingresar S o N")



      
