#Complejidad temporal O(n*m)
#Complejidad espacial O(n*m)
#n es el tamaño del arreglo y m es la suma objetivo

import time

time_start = time.perf_counter()
def ProgramacionDP(n, m):
    # dp[i] almacenará todas las combinaciones que suman i
    dp = [[] for _ in range(m + 1)]
    dp[0] = [[]]  # Caso base: suma 0 tiene una combinación vacía

    # Iterar sobre cada número en el conjunto
    for num in n:
        for j in range(m, num - 1, -1):
            for prev in dp[j - num]:
                dp[j].append(prev + [num])

    return dp[m]

# Prueba
n = [93, 7, 15, 1, 35, 5, 21, 47, 3, 55, 17, 9, 75, 29, 13, 43, 19, 31, 23, 11]
m = 100


result = ProgramacionDP(n, m)
time_elapsed = (time.perf_counter() - time_start)

print(f"Programacion Dinamica - Combinaciones: {result}")
print(f"Tiempo de ejecucion: {time_elapsed}")