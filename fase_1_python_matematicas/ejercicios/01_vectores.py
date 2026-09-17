"""
EJERCICIO 01: Vectores y una neurona simple

Objetivo
--------
Entender un vector como una lista de numeros y practicar las operaciones que
aparecen continuamente en inteligencia artificial.

Contexto
--------
En IA, una imagen, un texto o los datos de una persona se representan como
vectores: listas de numeros. Por ejemplo:

    persona = [25, 1.75, 70]

podria guardar edad, altura y peso.

Tu tarea
---------
1. Ejecuta este archivo con: python3 01_vectores.py
2. Lee y prueba estas operaciones:
   - sumar dos vectores
   - multiplicar un vector por un numero
   - calcular el producto punto
3. Cambia los vectores de ejemplo e intenta predecir cada resultado antes de
   ejecutar el programa.
4. Comprueba que entiendes distancia_manhattan: suma las diferencias absolutas
   entre las posiciones de dos vectores.
5. Observa neurona_simple. Una neurona basica calcula:

       salida = entradas . pesos + bias

   El producto punto decide cuanto aporta cada entrada; el bias ajusta el
   resultado final.

Al terminar, deberias poder explicar con tus palabras que es un vector, que
hace el producto punto y por que esa formula puede representar una decision.
"""





# Suma dos vectores posicion por posicion.
# Ejemplo: [1, 2, 3] + [4, 5, 6] -> [5, 7, 9]
def sumar_vectores(a, b):
    if len(a) != len(b): # tienen a y b distinta cantidad de elementos?
        raise ValueError("Los vectores deben tener la misma longitud")# si se cumple lanzamos un error

    resultado = [] #lista vacia donde guardar los numeros
    for i in range(len(a)):
        resultado.append(a[i] + b[i]) # en cada posición sumamos los elementos equivalente de ambos vectores y a la lista
    return resultado


# Multiplica todos los valores de un vector por un numero.
# Ejemplo: [1, 2, 3] * 10 -> [10, 20, 30]
def multiplicar_por_escalar(vector_a, escalar): # escalar =10 
    resultado = []
    for valor in vector_a:
        resultado.append(valor * escalar) # multiplicamos los 3 valores por 10
    return resultado


# Multiplica los valores que estan en la misma posicion y suma los resultados.
# Ejemplo: [1, 2, 3] y [4, 5, 6] -> (1*4) + (2*5) + (3*6) = 32
def producto_punto(a, b):
    if len(a) != len(b):
        raise ValueError("Los vectores deben tener la misma longitud") #como antes si no tienen misma longitud error

    total = 0
    for i in range(len(a)):
        total += a[i] * b[i] # multiplica los números que están en la misma posición y suma 
    return total



# Mide la distancia entre dos vectores sumando las diferencias absolutas posicion por posicion.
# Ejemplo: [1, 2, 3] y [4, 5, 6] -> abs(1-4) + abs(2-5) + abs(3-6) = 9
def distancia_manhattan(a, b):
    if len(a) != len(b):
        raise ValueError("Los vectores deben tener la misma longitud")
    totalManhattan = 0
    for i in range(len(a)):
        totalManhattan += abs(a[i]-b[i])
    return totalManhattan        


# Calcula la salida de una neurona simple usando vectores.
# entradas y pesos son vectores: se hace su producto punto y luego se suma el bias.
# Ejemplo: producto_punto(entradas, pesos) + bias
def neurona_simple(entradas, pesos, bias):
    return producto_punto(entradas, pesos) + bias
# (0.8 * 0.5) + (0.4 * -0.2) + (0.9 * 0.7) + 0.1

if __name__ == "__main__":
    vector_a = [1, 2, 3]
    vector_b = [4, 5, 6]

    print("Vector A:", vector_a)
    print("Vector B:", vector_b)
    print("Suma:", sumar_vectores(vector_a, vector_b)) # devuelve resultado
    print("A * 10:", multiplicar_por_escalar(vector_a, 10))
    print("Producto punto:", producto_punto(vector_a, vector_b))
    print("Distancia_manhattan",distancia_manhattan(vector_a,vector_b))

    entradas = [0.8, 0.4, 0.9]
    pesos = [0.5, -0.2, 0.7]
    bias = 0.1

    print("Neurona simple:", neurona_simple(entradas, pesos, bias))
