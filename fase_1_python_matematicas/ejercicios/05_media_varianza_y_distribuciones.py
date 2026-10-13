"""
EJERCICIO 05: Media, varianza y distribuciones

Objetivo
--------
Calcular el promedio de unos datos y ver cuanto se separan de ese promedio.
Entender una distribucion como la forma en que se reparten los valores.

Ejemplo
-------
Para [2, 4, 6] la media es 4.
La varianza es ((2 - 4)**2 + (4 - 4)**2 + (6 - 4)**2) / 3 = 8 / 3.
La desviacion estandar es la raiz cuadrada de esa varianza.

Para practicar
--------------
1. Ejecuto este archivo con: python3 05_media_varianza_y_distribuciones.py
2. Cambio los datos y veo como cambian la media y la varianza.
3. Comparo dos listas con la misma media y distinta dispersion.
4. Cambio la media y la desviacion de la simulacion normal y vuelvo a probar.

Idea clave
----------
En IA uso estas medidas para entender los datos antes de entrenar un modelo.
Aqui calculo la varianza poblacional: divido entre el numero de datos, n.
Si estimara la varianza de una poblacion a partir de una muestra, usaria n - 1.
"""

import math  # uso math para calcular la raiz cuadrada
import random  # uso random para generar datos de ejemplo


def media(datos):
    if not datos:
        raise ValueError("La lista de datos no puede estar vacia")

    total = 0
    for valor in datos:
        total += valor  # voy sumando todos los valores
    return total / len(datos)  # divido la suma entre la cantidad de datos


def varianza(datos):
    promedio = media(datos)  # primero necesito saber donde esta la media
    total = 0
    for valor in datos:
        diferencia = valor - promedio  # calculo cuanto se separa este valor de la media
        total += diferencia ** 2  # elevo al cuadrado para que las diferencias no se cancelen
    return total / len(datos)  # saco el promedio de esas diferencias al cuadrado


def desviacion_estandar(datos):
    # saco la raiz de la varianza para volver a las mismas unidades que los datos
    return math.sqrt(varianza(datos))


def distribucion_frecuencias(datos):
    if not datos:
        raise ValueError("La lista de datos no puede estar vacia")

    frecuencias = {}  # aqui guardo cada valor y las veces que aparece
    for valor in datos:
        if valor not in frecuencias:  # es la primera vez que encuentro este valor?
            frecuencias[valor] = 0
        frecuencias[valor] += 1  # sumo una aparicion de este valor

    distribucion = {}
    for valor, cantidad in frecuencias.items():
        distribucion[valor] = cantidad / len(datos)  # paso el recuento a una frecuencia relativa
    return distribucion


def generar_normal(cantidad, promedio=0, desviacion=1, semilla=42):
    if cantidad <= 0:
        raise ValueError("Tengo que generar al menos un dato")
    if desviacion <= 0:
        raise ValueError("La desviacion debe ser mayor que cero")

    generador = random.Random(semilla)  # fijo la semilla para poder repetir el ejemplo
    datos = []
    for _ in range(cantidad):
        # genero un valor de una distribucion normal, con forma de campana
        # la media marca el centro y la desviacion indica cuanto se dispersan los valores
        datos.append(generador.gauss(promedio, desviacion))
    return datos


if __name__ == "__main__":
    datos = [2, 4, 6]
    print("Datos:", datos)
    print("Media:", media(datos))  # aqui me da 4
    print("Varianza:", varianza(datos))  # aqui me da 8 / 3, aproximadamente 2.6667
    print("Desviacion estandar:", desviacion_estandar(datos))  # aproximadamente 1.633

    # las dos listas tienen media 4, pero en la segunda los valores estan mas separados
    datos_juntos = [3, 4, 5]
    datos_separados = [0, 4, 8]
    for ejemplo in [datos_juntos, datos_separados]:
        print(f"Datos {ejemplo}: media = {media(ejemplo)}, varianza = {varianza(ejemplo)}")

    # cuento resultados de ejemplo de un dado, no son las probabilidades exactas del dado
    tiradas = [1, 2, 2, 3, 4, 4, 4, 5, 6, 6]
    distribucion = distribucion_frecuencias(tiradas)
    print("Frecuencias relativas del dado:", distribucion)
    print("Suma de las frecuencias:", sum(distribucion.values()))  # me tiene que dar casi 1

    # en un dado justo la distribucion teorica es uniforme: cada cara tiene probabilidad 1 / 6
    uniforme = {}
    for cara in range(1, 7):
        uniforme[cara] = 1 / 6
    print("Distribucion uniforme de un dado justo:", uniforme)

    # ahora genero 1000 datos de una normal con media 10 y desviacion 2
    datos_normales = generar_normal(1000, promedio=10, desviacion=2)
    print("Media de los datos normales:", media(datos_normales))  # espero un valor cercano a 10
    print("Varianza de los datos normales:", varianza(datos_normales))  # espero cerca de 2**2 = 4
    print("Desviacion de los datos normales:", desviacion_estandar(datos_normales))
    # no me salen valores exactos porque estoy midiendo una muestra aleatoria
