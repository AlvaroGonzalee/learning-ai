"""
EJERCICIO 02: Matrices y matrices por vectores

Objetivo
--------
Aprender a trabajar con una matriz: una tabla de numeros formada por filas y
columnas. Las matrices permiten guardar muchos datos o hacer varios calculos
con vectores a la vez.

Ejemplo
-------
Una matriz de 2 filas y 3 columnas se escribe asi:

    matriz = [
        [1, 2, 3],
        [4, 5, 6],
    ]

La primera fila es [1, 2, 3]. La primera columna contiene 1 y 4.

Tu tarea
---------
1. Ejecuta este archivo con: python3 02_matrices.py
2. Cambia los numeros de las matrices e intenta adivinar el resultado antes
   de ejecutar.
3. Revisa como multiplicar_matriz_por_vector calcula un producto punto por
   cada fila.
4. Completa transponer_matriz al final del archivo. Transponer cambia filas
   por columnas. Por ejemplo:

       [[1, 2, 3], [4, 5, 6]]  ->  [[1, 4], [2, 5], [3, 6]]

Idea clave
----------
Una capa de una red neuronal puede guardar los pesos de varias neuronas en una
matriz. Al multiplicarla por las entradas, cada fila produce la salida de una
neurona.
"""


def validar_matriz(matriz):
    """Comprueba que todas las filas tengan el mismo numero de columnas."""
    if not matriz:
        raise ValueError("La matriz no puede estar vacia")

    columnas = len(matriz[0])
    if columnas == 0:
        raise ValueError("Las filas no pueden estar vacias")

    for fila in matriz:
        if len(fila) != columnas:
            raise ValueError("Todas las filas deben tener la misma longitud")


# Suma dos matrices posicion por posicion.
# Ejemplo: [[1, 2], [3, 4]] + [[5, 6], [7, 8]] -> [[6, 8], [10, 12]]
def sumar_matrices(a, b):
    validar_matriz(a)
    validar_matriz(b)

    if len(a) != len(b) or len(a[0]) != len(b[0]):
        raise ValueError("Las matrices deben tener las mismas dimensiones")

    resultado = []
    for i in range(len(a)):
        fila_resultado = []
        for j in range(len(a[0])):
            fila_resultado.append(a[i][j] + b[i][j])
        resultado.append(fila_resultado)
    return resultado


# Multiplica cada numero de una matriz por un escalar.
# Ejemplo: [[1, 2], [3, 4]] * 10 -> [[10, 20], [30, 40]]
def multiplicar_matriz_por_escalar(matriz, escalar):
    validar_matriz(matriz)

    resultado = []
    for fila in matriz:
        fila_resultado = []
        for valor in fila:
            fila_resultado.append(valor * escalar)
        resultado.append(fila_resultado)
    return resultado


# Multiplica una matriz por un vector.
# Cada fila de la matriz se multiplica por el vector y se suman los resultados.
# Ejemplo: [[1, 2, 3], [4, 5, 6]] * [2, 1, 0] -> [4, 13]
def multiplicar_matriz_por_vector(matriz, vector):
    validar_matriz(matriz)

    if len(matriz[0]) != len(vector):
        raise ValueError("El vector debe tener un valor por cada columna")

    resultado = []
    for fila in matriz:
        total = 0
        for i in range(len(fila)):
            total += fila[i] * vector[i]
        resultado.append(total)
    return resultado


#Una nueva fila por cada columna de la matriz original.
def transponer_matriz(matriz):
    validar_matriz(matriz)

    resultado = []
    for columna in range(len(matriz[0])):
        nueva_fila = []
        for fila in matriz:
            nueva_fila.append(fila[columna])
        resultado.append(nueva_fila)
    return resultado


if __name__ == "__main__":
    matriz_a = [
        [1, 2, 3],
        [4, 5, 6],
    ]
    matriz_b = [
        [10, 20, 30],
        [40, 50, 60],
    ]
    vector = [2, 1, 0]

    print("Matriz A:", matriz_a)
    print("Matriz B:", matriz_b)
    print("A + B:", sumar_matrices(matriz_a, matriz_b))
    print("A * 10:", multiplicar_matriz_por_escalar(matriz_a, 10))
    print("A * vector:", multiplicar_matriz_por_vector(matriz_a, vector))
    print("Matriz A transpuesta:", transponer_matriz(matriz_a))
