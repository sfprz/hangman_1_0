# hangman_1_0

- Dana Sofia Perez Loaiza
- sofia.perez7@utp.edu.co

## Lista de tareas
### Inicio
- [X] genera una palabra oculta seleccionada aleatoriamente
- [X] reemplaza cada carácter por el símbolo “_”
- [X] pide al usuario que ingrese una letra por consola 
### Verificación de la letra
- [X] verifica que sea solo una letra 
- [X] verifica si la letra se encuentra entre la A y Z
- [X] verifica si la letra no se ha utilizado previamente 
- [X] verifica si la letra existe en la palabra
- [X] La letra existe: reemplaza el guion una o varias veces
- [ ] La letra no existe: Borra una de las 6 vidas 
- [ ] La letra no existe: comienza el dibujo 
- [ ] La letra no existe: muestra las vidas faltantes al jugador
### Creacion del muñeco 
- [ ] Crear en un archivo aparte las 6 etapas del monigote con símbolos
- [ ] Importar el archivo del monigote en el programa principal
- [ ] Mostrar la etapa del dibujo que corresponde a los errores del jugador
### Fin de la partida 
- [ ] Si el jugador adivina la palabra: presenta el mensaje “ganaste”
- [ ] Si el jugador pierde las 6 vidas: presenta el mensaje “perdiste”
- [ ] Si el jugador pierde las 6 vidas: presenta contador en 0
- [ ] Si el jugador pierde las 6 vidas: Termina el dibujo 
- [ ] Si el jugador pierde las 6 vidas: Destapa la palabra oculta
- [ ] Al terminar (no importa si gana o pierde): muestra la opción de volver a jugar o finalizar (cerrar el programa)
### Ciclo del juego
- [ ] Repetir el turno (pedir letra, validar, revisar) mientras el jugador tenga vidas y no haya adivinado la palabra
- [ ] Mostrar la palabra oculta con sus guiones y letras acertadas después de cada turno
### Victoria y derrota
- [ ] Detectar que el jugador ganó cuando ya no quedan guiones en la palabra oculta
- [ ] Detectar que el jugador perdió cuando las vidas llegan a 0
### Volver a jugar
- [ ] Validar que la respuesta del menú final sea una de las dos opciones permitidas
- [ ] Si elige jugar de nuevo, reiniciar todo (nueva palabra, vidas, letras usadas)
- [ ] Si elige finalizar, cerrar el programa
### Estructura y entrega
- [ ] Carpeta del programa llamada `hangman_1_0` con 3 archivos (principal, palabras y dibujo)
- [ ] Repositorio público en GitHub, con un commit por cada requerimiento
- [ ] README con nombre, correo y cómo ejecutar el programa
- [ ] README con encabezados y Alert Types

> [!NOTE] Se aceptan solo palabras de la A a la Z sin contar la Ñ o las tildes. 