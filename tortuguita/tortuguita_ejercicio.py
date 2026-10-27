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
tortuga.shape("turtle")
tortuga.speed(5)
tortuga.pensize(3)


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

while True:
    instruccion = input(
        "Instrucción (arriba, abajo, izquierda, derecha, "
        "lapiz_arriba, lapiz_abajo, limpiar, salir): "
    )
    instruccion = instruccion.strip().lower()

    # TODO: agregar la condición de salida y las condiciones para cada comando.
    pass


pantalla.mainloop()
