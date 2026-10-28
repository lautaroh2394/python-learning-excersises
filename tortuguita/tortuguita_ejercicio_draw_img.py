"""Ejercicio de ciclos: interpretar instrucciones para mover una tortuguita.

Completá el ciclo de instrucciones al final del archivo.
Comandos sugeridos: arriba, abajo, izquierda, derecha, lapiz_arriba,
lapiz_abajo, limpiar y salir.
"""

import turtle
from PIL import Image

# Abrir imagen
im = Image.open("gay.png")
data = im.getdata()

# Configuración de la ventana y la tortuguita.
pantalla = turtle.Screen()
pantalla.title("La tortuguita")

screen_w = im.width * 6
screen_h = im.height * 6
pantalla.setup(width=screen_w, height=screen_h)


tortuga = turtle.Turtle()
tortuga.shape("square")
tortuga.speed(5)
tortuga.pensize(2)

start_x = - screen_w/2 + im.width 
start_y = screen_h/2 - im.height

# Funciones de movimiento. Cada movimiento avanza 40 píxeles.
def MoverArriba():
    tortuga.setheading(90)
    tortuga.forward(4)


def MoverAbajo():
    tortuga.setheading(270)
    tortuga.forward(4)


def MoverIzquierda():
    tortuga.setheading(180)
    tortuga.forward(4)


def MoverDerecha():
    tortuga.setheading(0)
    tortuga.forward(4)

def MoverAInicioX():
    tortuga.setpos(start_x,tortuga.pos()[1])

def MoverAInicioY():
    tortuga.setpos(tortuga.pos()[0],start_y)

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

def DibujarPunto():
    tortuga.dot()

LevantarLapiz()
MoverAInicioX()
MoverAInicioY()


for y in range(0, im.height):
    for x in range(0, im.width):
        MoverDerecha()
        curr_pos = y * im.width + x
        curr = data[curr_pos] 

        r = curr[0] 
        g = curr[1] 
        b = curr[2] 
        
        if not (r == 255 and g == 255 and b == 255):
            DibujarPunto()
            
    MoverAbajo()
    MoverAInicioX()

pantalla.mainloop()
