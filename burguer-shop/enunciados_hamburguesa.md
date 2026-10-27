# LAUTI'S EL GORDO BURGUER SHOP

Bienvenida a mi nueva hamburguesería, "el gordo burguer shop". Estamos por abrir y necesitamos un programa para facilitarle a los clientes el pedido de hamburguesas.
Necesito que armes un programa en python que haga lo siguiente. Sólo cuando termines con un punto podés avanzar al que le sigue.

## 1. Elegir cada ingrediente

Tenemos un script `hamburguesa_esqueleto.py` donde vas a tener que implementar lo que necesitamos. Hay algunas cosas ahí que te van a servir.
Completá `hamburguesa_esqueleto.py` para que el programa pregunte al usuario si va a querer en su hamburguesa:
    - lechuga
    - tomate
    - queso
    - carne. 

Por cada ingrediente el programa hace una pregunta al usuario.
Para cada respuesta afirmativa, llamá a la función que dibuja ese ingrediente. Si responde que no, el ingrediente no debe aparecer.

Al final, el programa debe mostrar una hamburguesa con pan arriba y abajo, y solo las capas que la persona eligió.

Para dibujar una capa, llamá a la función correspondiente, por ejemplo: `dibujarLechuga()`.
Probá distintas combinaciones, incluyendo decir que no a todos los ingredientes.

Podés ejecutar el script en la consola escribiendo: `python burguer-shop/hamburguesa_esqueleto.py`

## 2. Elegir cantidad de carnes

Si al preguntarle al usuario si quiere carne este responde afirmativamente, preguntar cuántas hamburguesas quiere y dibujar esa cantidad de capas.

## 3. Limitar la cantidad máxima de carnes

A nuestro cocinero se le desarma la hamburguesa cuando es muy alta; solo hacerla de máximo 4 carnes. Si el usuario quiere más de 4 carnes, servirle cuatro.

## 4. Crear combos

Contratamos a Emi, un loquito de las hamburguesas y dice que conoce las mejores combinaciones. El tipo se armó "combos": hamburguesas con las capas ya definidas.

Antes de preguntar los ingredientes, ofrecele al usuario combos ya creados:
    - Vegetariana: lechuga, tomate, lechuga, tomate
    - Clásica: lechuga, tomate, carne, carne
    - Completa: lechuga, tomate, queso, carne

En caso que no quiera un combo, proceder con las preguntas sobre los ingredientes normalmente.

## 5. Usar una función para preguntar

Escribir una función "consultarIngrediente" que reciba un ingrediente, consulte al usuario si quiere ese ingrediente, y retorne la respuesta del usuario como booleano.
Reemplazar las consultas ya hechas anteriormente sobre los ingredientes para que se hagan usando esta función.

## 6. Mejora: guardar las capas y dibujar al final

En vez de dibujar cada capa inmediatamente después de cada pregunta al usuario, guardar una lista de ingredientes y dibujar la hamburguesa al final, luego de las preguntas:
Guardá las capas elegidas en una lista. Después de hacer todas las preguntas, recorré la lista y dibujá cada capa en el orden correcto. Así, las preguntas y el dibujo quedan separados.

## 3. Variación: indicar los ingredientes

Nos cansamos de los pelotudos de los clientes; siete horas tardan los boludos para decir "si" o "no" a preguntas boludísimas. Ahora que vengan directamente con los ingredientes pensados y nos ahorramos la frustración.

En vez de preguntar sí o no para cada ingrediente, pedile a la persona que escriba los ingredientes que quiere, separados por comas; por ejemplo: `carne, queso, lechuga`. Procesá esa respuesta y dibujá las capas elegidas.

## 8. Mejora: validación de ingredientes

Nunca falta alguien que sobra; cayó un salame que trajo una lista de ingredientes que incluía sopa de banana. Hay que ser pelotudo.

Antes de armar la hamburguesa, validá los ingredientes que indicó el usuario. Si alguno de los ingredientes no es válido (es decir, no lo ofrecemos), la hamburguesa no es posible de hacer. Indicarle al usuario esto mismo con un mensaje y a otra cosa mariposa.

## 9 . Aceptá mayúsculas y espacios extra

Algunas personas no saben escribir como corresponde. Asegurate de aceptar ingredientes con mayúsculas y/o espacios de más.
Ejemplos de listas de ingredientes válidas:
    - "carne  , QUESO , TomaTe"
    - "lechuga,tomate,queso"
    -"QUesO ,   caRnE     "
