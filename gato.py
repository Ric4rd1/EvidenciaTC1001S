import turtle
from freegames import line

t = turtle.Turtle()


def grid():
    """Dibuja la cuadricula del tic-tac-toe."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):
    """Dibujar X para el jugador."""
    t.pencolor("pink")
    t.pensize(3)
    line(x + 40, y + 30, x + 133, y + 133)
    line(x + 40, y + 133, x + 133, y + 30)


def drawo(x, y):
    """Dibujar O para el jugador."""
    t.pencolor("green")
    t.pensize(3)
    t.up()
    t.goto(x + 68, y + 16)
    t.down()
    t.circle(48)


def floor(value):
    """Redondea el valor de la cuadricula a 133."""
    return ((value + 200) // 133) * 133 - 200


state = {'player': 0}
players = [drawx, drawo]


def tap(x, y):
    """Dibuja X o O en el cuadro que sea clikeado."""
    x = floor(x)
    y = floor(y)
    player = state['player']
    draw = players[player]
    if (x, y) not in vis:
        vis[(x, y)] = True
        draw(x, y)
    t.update()
    state['player'] = not player


vis = {}
t.setup(420, 420, 370, 0)
t.hideturtle()
t.tracer(False)
t.grid()
t.update()
t.onscreenclick(tap)
t.done()
