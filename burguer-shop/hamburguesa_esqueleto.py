"""Esqueleto para practicar if/else dibujando una hamburguesa."""


def dibujarPanSuperior():
    print("   _________")
    print(" /         \\")


def dibujarLechuga():
    print(" ~~~~~~~~~~~")


def dibujarTomate():
    print("  o  o  o  o")


def dibujarQueso():
    print("  /-------/")


def dibujarCarne():
    print("  =========")


def dibujarPanInferior():
    print(" \\_________/")

def atenderCliente():
    respuesta = input("Bienvenido a El Gordo burguer shop! Vamos a armar una hamburguesa? (s/n): ").strip().lower()
    if respuesta != "s":
        print("Ah... bueno :c")
        return

    print("Buenísimo c:")

    dibujarPanSuperior()

    respuesta = input("¿Quiere tomate? (s/n): ").strip().lower()
    if respuesta == "s":
        # TODO: llamar a la función que dibuja el tomate
        pass
    else:
        pass

    # TODO: Agregar el resto de ingredientes


    dibujarPanInferior()

    print("Lista la burgaa!")

atenderCliente()