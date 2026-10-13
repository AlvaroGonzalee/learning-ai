"""
EJERCICIO 04: Probabilidad basica

Objetivo
--------
Entender la probabilidad como un numero entre 0 y 1:
0 significa imposible y 1 significa seguro. Un 0.5 equivale al 50%.

Ejemplo
-------
En un dado justo hay 6 resultados igual de probables.
Los pares son 2, 4 y 6: la probabilidad de un par es 3 / 6 = 0.5.

Para practicar
--------------
1. Ejecuto este archivo con: python3 04_probabilidad_basica.py
2. Cambio los numeros del evento y predigo la probabilidad antes de ejecutar.
3. Comparo la probabilidad exacta de cara con una simulacion de lanzamientos.
4. Pruebo con 10, 100 y 1000 lanzamientos para ver como cambia el resultado.

Idea clave
----------
En IA uso probabilidades para representar incertidumbre. Aqui empiezo con
dados y monedas justos, donde puedo contar los resultados posibles.
"""

import random  # uso random para simular lanzamientos


def probabilidad(casos_favorables, casos_posibles):
    if casos_posibles <= 0:  # tengo que tener al menos un caso posible
        raise ValueError("Los casos posibles deben ser mayores que cero")
    if casos_favorables < 0 or casos_favorables > casos_posibles:
        raise ValueError("Los casos favorables deben estar entre 0 y los posibles")

    # divido los casos que me sirven entre todos los posibles
    # esta formula la uso cuando todos los resultados son igual de probables
    return casos_favorables / casos_posibles


def probabilidad_evento(resultados, evento):
    favorables = 0
    for resultado in resultados:
        if resultado in evento:  # este resultado esta entre los que busco?
            favorables += 1  # si se cumple lo cuento como favorable
    return probabilidad(favorables, len(resultados))


def simular_moneda(lanzamientos, semilla=42):
    if lanzamientos <= 0:
        raise ValueError("Tengo que hacer al menos un lanzamiento")

    # fijo una semilla para repetir la misma simulacion cuando ejecuto el archivo
    generador = random.Random(semilla)
    caras = 0
    for _ in range(lanzamientos):  # uso _ porque solo me interesa repetir, no el indice
        resultado = generador.choice(["cara", "cruz"])
        if resultado == "cara":
            caras += 1
    # calculo la frecuencia de caras que he observado, puede no salir justo 0.5
    return caras / lanzamientos


if __name__ == "__main__":
    dado = [1, 2, 3, 4, 5, 6]
    pares = [2, 4, 6]
    probabilidad_par = probabilidad_evento(dado, pares)
    print("Probabilidad de un par:", probabilidad_par)  # aqui me tiene que dar 0.5
    print("Porcentaje de un par:", probabilidad_par * 100, "%")

    # para el evento contrario resto la probabilidad a 1
    print("Probabilidad de un impar:", 1 - probabilidad_par)

    # si las monedas son independientes, multiplico las probabilidades
    # que salga cara en la primera no cambia la probabilidad de la segunda
    print("Probabilidad de dos caras con dos monedas:", probabilidad(1, 2) ** 2)

    # aqui creo todos los resultados posibles de lanzar dos dados justos
    resultados_dos_dados = []
    for primero in dado:
        for segundo in dado:
            resultados_dos_dados.append((primero, segundo))  # guardo una pareja por resultado

    # ahora se que el primer dado es par, asi que solo me quedo con esos casos
    # esto es una probabilidad condicionada: uso la informacion que ya tengo
    casos_con_primer_par = []
    casos_con_suma_mayor_8 = []
    for primero, segundo in resultados_dos_dados:
        if primero in pares:
            casos_con_primer_par.append((primero, segundo))
            if primero + segundo > 8:
                casos_con_suma_mayor_8.append((primero, segundo))

    print("P(suma > 8 sabiendo que el primer dado es par):",
          probabilidad(len(casos_con_suma_mayor_8), len(casos_con_primer_par)))
    print("Resultado esperado: 6 / 18, aproximadamente 0.3333")

    for cantidad in [10, 100, 1000]:
        print(f"Frecuencia de caras en {cantidad} lanzamientos:", simular_moneda(cantidad))
    # con mas lanzamientos suele acercarse a 0.5, pero no tiene que mejorar en cada prueba
