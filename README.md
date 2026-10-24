# hangman_1_0

- Dana Sofia Perez Loaiza
- sofia.perez7@utp.edu.co

## Lista de tareas
### Inicio
- [X] genera una palabra oculta seleccionada aleatoriamente
- [X] reemplaza cada carácter por el símbolo “_”
- [X] pide al usuario que ingrese una letra por consola 
- [X] Importar el archivo de palabras en el programa principal
### Verificación de la letra
- [X] verifica que sea solo una letra 
- [X] verifica si la letra se encuentra entre la A y Z
- [X] verifica si la letra no se ha utilizado previamente 
- [X] verifica si la letra existe en la palabra
- [X] La letra existe: reemplaza el guion una o varias veces
- [X] La letra no existe: borra una de las 6 vidas 
- [X] La letra no existe: comienza el dibujo 
- [X] La letra no existe: muestra las vidas faltantes al jugador
### Creacion del muñeco 
- [X] Crear en un archivo aparte las 6 etapas del dibujo con símbolos
- [X] Importar el archivo del dibujo en el programa principal
- [X] Mostrar la etapa del dibujo que corresponde a los errores del jugador
### Fin de la partida 
- [X] Si el jugador adivina la palabra: presenta el mensaje “ganaste”
- [X] Si el jugador pierde las 6 vidas: presenta el mensaje “perdiste”
- [X] Si el jugador pierde las 6 vidas: presenta contador en 0
- [X] Si el jugador pierde las 6 vidas: Termina el dibujo 
- [X] Si el jugador pierde las 6 vidas: Destapa la palabra oculta
- [X] Al terminar (no importa si gana o pierde): muestra la opción de volver a jugar o finalizar (cerrar el programa)
### Ciclo del juego
- [X] Repetir el turno (pedir letra, validar, revisar) mientras el jugador tenga vidas y no haya adivinado la palabra
- [X] Mostrar la palabra oculta con sus guiones y letras acertadas al inicio de cada turno
### Victoria y derrota
- [X] Detectar que el jugador ganó cuando ya no quedan guiones en la palabra oculta
- [X] Detectar que el jugador perdió cuando las vidas llegan a 0
### Volver a jugar
- [X] Validar que la respuesta del menú final sea una de las dos opciones permitidas
- [X] Si elige jugar de nuevo, reiniciar todo (nueva palabra, vidas, letras usadas)
- [X] Si elige finalizar, cerrar el programa
### Estructura y entrega
- [X] Carpeta del programa llamada `hangman_1_0` con 3 archivos (principal, palabras y dibujo)
- [X] Repositorio público en GitHub, con un commit por cada requerimiento
- [ ] README con nombre, correo y cómo ejecutar el programa
- [ ] README con encabezados y Alert Types

> [!NOTE] 
> Se aceptan solo letras de la A a la Z sin contar la Ñ o las tildes. 
> [!NOTE] 
> Las etapas del dibujo estan desde 0 siendo la horca vacia y 6 siendo el muñeco completo, para que las posiciones de las vidas vayan acorde de 1 a 6 