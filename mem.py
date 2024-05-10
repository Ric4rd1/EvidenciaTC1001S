"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""

from random import shuffle
from turtle import *
from freegames import path

# Cargar la imagen del carro
car = path('car.gif')
# Lista de números para las fichas del juego 
tiles = list(range(32)) * 2
# Estado del juego 
state = {'mark': None}
# Lista para ocultar las fichas
hide = [True] * 64

# Contador de Taps
num_taps = 0

# Detectar cuando todas las cajas han sido descubiertas
all_uncovered = False

def square(x, y):
    """Dibuja un cuadro blanco con contorno negro en (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for _ in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convierte las coordenadas (x,y) en el índice de las fichas."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convierte el contador de fichas en las coordenadas (x, y)."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Actualizar marcas y mosaicos ocultos según el tap."""
    global num_taps, all_uncovered
    num_taps +=1 #incrementar el número de taps

    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

    # Compruebe si se han descubierto todas las casillas
    if all (not hidden for hidden in hide):
        all_uncovered = True

def draw():
    """Dibujar imagen y mosaicos."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    # Mostrar el número de taps 
    up()
    goto(-150, 200)
    write(f"Taps: {num_taps}", font=('Arial', 20, 'normal'))

    # Mostrar un mensaje si se han descubierto todas las casillas
    if all_uncovered:
        up()
        goto(0, -160) # Posición ajustada
        color('green')
        write("Felicidades!\nDescubriste la imagen!", align='center', font=('Arial', 14, 'normal')) #Tamaño de fuente ajusatado

    update()
    ontimer(draw, 100)

# Mezclar las fichas
shuffle(tiles)
# Configurar la ventana
setup(420, 420, 370, 0)
# Añadir la imagen del carro
addshape(car)
# Ocultar el cursos de la tortuga 
hideturtle()
# Desactivar la animación de la tortuga
tracer(False)
# Configurar la función de click en pantalla
onscreenclick(tap)
# Dibujar el juego
draw()
# Finalizar el juego
done()