#complejidad temporal O(2^n)
#complejidad espacial O(2^n)

import time

# Algoritmo 5: por Backtracking
def encontrar_combinaciones(arr, M, index=0, suma_actual=0, combinacion=[]):
    if suma_actual == M:
        print(combinacion)  # Se encontró una combinación
        return
    
    if index >= len(arr) or suma_actual > M:
        return
    
    # Opción 1: Incluir arr[index] en la combinación
    encontrar_combinaciones(arr, M, index + 1, suma_actual + arr[index], combinacion + [arr[index]])
    
    # Opción 2: No incluir arr[index] y pasar al siguiente
    encontrar_combinaciones(arr, M, index + 1, suma_actual, combinacion)

# Ejemplo de uso
conjunto = [93, 7, 15, 1, 35, 5, 21, 47, 3, 55, 17, 9, 75, 29, 13, 43, 19, 31, 23, 11]
M = 100

# Medir el tiempo de ejecución
inicio = time.time()
encontrar_combinaciones(conjunto, M)
fin = time.time()

print(f"Tiempo de ejecución: {fin - inicio} segundos")
