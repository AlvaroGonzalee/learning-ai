"""
EJERCICIO 03: Funciones y derivadas numericas

Objetivo
--------
Entender una funcion como una regla que transforma una entrada en una salida,
y usar una derivada numerica para medir cuanto cambia esa salida.

Ejemplos
--------
    f(x) = 2 * x + 1
    f(3) = 7

    g(x) = x * x
    g(3) = 9

La derivada responde a esta pregunta: si muevo x un poquito, cuanto cambia el
resultado? Para g(x) = x * x, en x = 3 la derivada es 6. Cerca de ese punto,
si x aumenta 0.01, la salida aumenta aproximadamente 0.06.

Tu tarea
---------
1. Ejecuta este archivo con: python3 03_funciones_y_derivadas.py
2. Cambia el valor de x y predice los resultados antes de ejecutar.
3. Observa que derivada_numerica prueba la funcion a cada lado de x:

       derivada ~= (f(x + h) - f(x - h)) / (2 * h)

   h es un numero muy pequeno.
4. Completa cubica(x). Despues, calcula su derivada en x = 2. El resultado
   esperado es aproximadamente 12.

Idea clave
----------
Durante el entrenamiento de una red neuronal, la derivada indica en que
direccion y cuanto conviene modificar los pesos para reducir un error.
"""


# f(x) = pendiente * x + bias
# aqui uso la misma formula que en la neurona simple
def funcion_lineal(x, pendiente, bias):
    # multiplico x por la pendiente y luego le sumo el bias
    return pendiente * x + bias  # si pongo x = 3, pendiente = 2 y bias = 1 me da 2 * 3 + 1 = 7


# f(x) = x al cuadrado
def cuadrado(x):
    return x * x  # multiplico x por si misma, si pongo 3 me da 3 * 3 = 9


# aqui calculo aproximadamente cuanto cambia una funcion cerca de un valor de x
def derivada_numerica(funcion, x, h=0.0001):
    # recibo la funcion que quiero probar y uso h como un paso muy pequeno
    valor_derecha = funcion(x + h)  # le sumo h a x y calculo el resultado
    valor_izquierda = funcion(x - h)  # ahora le resto h a x y calculo el otro resultado
    # resto ambos resultados y divido entre 2 * h, que es la distancia entre los dos puntos
    # con esto veo cuanto cambia la salida por cada unidad que cambia x
    # si uso el cuadrado con x = 3 hago (3.0001**2 - 2.9999**2) / 0.0002 y me da casi 6
    return (valor_derecha - valor_izquierda) / (2 * h)


# f(x) = x al cubo
def cubica(x):
    return x ** 3  # uso ** para elevar x al cubo, si pongo 2 me da 2 * 2 * 2 = 8


# aqui pruebo las funciones cuando ejecuto este archivo directamente
# si lo importo desde otro archivo, estas pruebas no se ejecutan
if __name__ == "__main__":
    x = 3  # pongo 3 para probar, luego puedo cambiarlo y ver que resultados me da

    print("x:", x)
    print("Funcion lineal 2x + 1:", funcion_lineal(x, 2, 1))
    print("Cuadrado de x:", cuadrado(x))
    # creo una funcion con un solo parametro para poder pasarla a derivada_numerica
    def lineal_ejemplo(x):
        return funcion_lineal(x, 2, 1)

    # en la recta, por cada unidad que aumento x la salida aumenta 2
    print("Derivada de 2x + 1:", derivada_numerica(lineal_ejemplo, x))
    print("Resultado esperado: aproximadamente 2")
    # paso cuadrado sin parentesis porque quiero pasar la funcion, no su resultado
    # la derivada de x al cuadrado es 2 * x, asi que con x = 3 me tiene que dar casi 6
    print(f"Derivada de x cuadrado en x = {x}:", derivada_numerica(cuadrado, x))
    print("Resultado esperado: aproximadamente", 2 * x)

    x_cubica = 2  # pongo 2 porque es el valor que me pide el reto
    print("Cubo de x en x = 2:", cubica(x_cubica))  # aqui compruebo que el cubo de 2 me da 8
    # la derivada de x al cubo es 3 * x**2, con x = 2 hago 3 * 4 y me da 12
    print("Derivada de x al cubo en x = 2:", derivada_numerica(cubica, x_cubica))
    print("Resultado esperado: aproximadamente", 3 * x_cubica ** 2)
    # si me sale 12.00000001 en vez de 12 es porque estoy calculando una aproximacion
