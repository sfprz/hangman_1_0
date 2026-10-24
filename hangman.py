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

