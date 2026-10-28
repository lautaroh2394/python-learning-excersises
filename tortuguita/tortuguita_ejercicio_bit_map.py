"""Ejercicio de ciclos: interpretar instrucciones para mover una tortuguita.

Completá el ciclo de instrucciones al final del archivo.
Comandos sugeridos: arriba, abajo, izquierda, derecha, lapiz_arriba,
lapiz_abajo, limpiar y salir.
"""

import turtle


# Configuración de la ventana y la tortuguita.
pantalla = turtle.Screen()
pantalla.title("La tortuguita")
pantalla.setup(width=700, height=500)

tortuga = turtle.Turtle()
tortuga.shape("square")
tortuga.speed(5)
tortuga.pensize(50)
tortuga.setpos(0,0)


# Funciones de movimiento. Cada movimiento avanza 40 píxeles.
def MoverArriba():
    tortuga.setheading(90)
    tortuga.forward(40)


def MoverAbajo():
    tortuga.setheading(270)
    tortuga.forward(40)


def MoverIzquierda():
    tortuga.setheading(180)
    tortuga.forward(40)


def MoverDerecha():
    tortuga.setheading(0)
    tortuga.forward(40)

def MoveToStartingX():
    tortuga.setpos(0,tortuga.pos()[1])

def MoveToStartingY():
    tortuga.setpos(tortuga.pos()[0],0)

# Funciones para controlar el lápiz y el dibujo.
def LevantarLapiz():
    tortuga.penup()


def BajarLapiz():
    tortuga.pendown()


def Limpiar():
    tortuga.clear()
    tortuga.penup()
    tortuga.home()
    tortuga.pendown()


# TODO: completar un ciclo que pida instrucciones hasta que la persona escriba
# "salir". Dentro del ciclo:
#   1. Pedir una instrucción con input().
#   2. Limpiar espacios y pasarla a minúsculas.
#   3. Usar if/elif para llamar a la función correspondiente.
#   4. Si no reconoce la instrucción, mostrar un mensaje y volver a preguntar.
#
# Ejemplo de una instrucción: "arriba" debe llamar a MoverArriba().
# Al terminar el ciclo, llamá a pantalla.mainloop() para que la ventana quede
# abierta hasta que la persona la cierre.

grid = [
    [1,1,1,1,1],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,1,1,1,1]
]

row = 0
MoveToStartingX()
MoveToStartingY()
for bits in grid:
    col = 0
    MoveToStartingX()
    for bit in bits:
        if bit == 1:
            BajarLapiz()
            MoverDerecha()
            LevantarLapiz()
        else:
            MoverDerecha()

        col+=1
    row+=1
    MoverAbajo()
    

pantalla.mainloop()
