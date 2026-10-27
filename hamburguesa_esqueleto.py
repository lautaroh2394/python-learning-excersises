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
    print("  _________")


print("Vamos a armar una hamburguesa.")
dibujarPanSuperior()

respuesta = input("¿Quiere lechuga? (s/n): ").strip().lower()
if respuesta == "s":
    # TODO: llamar a la función que dibuja la lechuga
    pass
else:
    pass

respuesta = input("¿Quiere tomate? (s/n): ").strip().lower()
if respuesta == "s":
    # TODO: llamar a la función que dibuja el tomate
    pass
else:
    pass

respuesta = input("¿Quiere queso? (s/n): ").strip().lower()
if respuesta == "s":
    # TODO: llamar a la función que dibuja el queso
    pass
else:
    pass

respuesta = input("¿Quiere carne? (s/n): ").strip().lower()
if respuesta == "s":
    # TODO: llamar a la función que dibuja la carne
    pass
else:
    pass

dibujarPanInferior()
