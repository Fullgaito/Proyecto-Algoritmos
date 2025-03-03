import time
import random
import numpy as np
import matplotlib.pyplot as plt
from itertools import combinations

# 🔹 Algoritmo Divide y Vencerás
def subsetSum_divconq(arr, index, current_subset, comb_list, sum_list):
    if index == len(arr):
        comb_list.append(current_subset[:])
        sum_list.append(sum(current_subset))
        return

    current_subset.append(arr[index])
    subsetSum_divconq(arr, index + 1, current_subset, comb_list, sum_list)

    current_subset.pop()
    subsetSum_divconq(arr, index + 1, current_subset, comb_list, sum_list)

def calcSubsets(n, arr, x):
    arr1, arr2 = arr[:n // 2], arr[n // 2:]

    comb1, sums1 = [], []
    subsetSum_divconq(arr1, 0, [], comb1, sums1)

    comb2, sums2 = [], []
    subsetSum_divconq(arr2, 0, [], comb2, sums2)

    for i in range(len(sums1)):
        for j in range(len(sums2)):
            if sums1[i] + sums2[j] == x:
                pass

# 🔹 Algoritmo de Fuerza Bruta
def subsetSum_force(n, arr, x):
    for i in range(n + 1):
        for subset in combinations(arr, i):
            if sum(subset) == x:
                pass

# 🔹 Algoritmo de Programación Dinámica
def ProgramacionDP(n, m):
    dp = [[] for _ in range(m + 1)]
    dp[0] = [[]]

    for num in n:
        for j in range(m, num - 1, -1):
            for prev in dp[j - num]:
                dp[j].append(prev + [num])

    return dp[m]

# 🔹 Algoritmo de Backtracking
def encontrar_combinaciones(arr, M, index=0, suma_actual=0, combinacion=[]):
    if suma_actual == M:
        return

    if index >= len(arr) or suma_actual > M:
        return

    encontrar_combinaciones(arr, M, index + 1, suma_actual + arr[index], combinacion + [arr[index]])
    encontrar_combinaciones(arr, M, index + 1, suma_actual, combinacion)

# 🔹 Prueba de rendimiento
def test_performance():
    sizes = list(range(2, 20, 2))  # Tamaños de prueba (de 2 a 20 en pasos de 2)
    num_trials = 5  # Para reducir variabilidad
    results = {"Divide y Vencerás": [], "Fuerza Bruta": [], "Programación Dinámica": [], "Backtracking": []}

    for size in sizes:
        arr = [random.randint(1, 50) for _ in range(size)]
        x = random.randint(5, 40)

        # 📌 Medir Divide y Vencerás
        times = []
        for _ in range(num_trials):
            start_time = time.perf_counter()
            calcSubsets(size, arr, x)
            times.append(time.perf_counter() - start_time)
        results["Divide y Vencerás"].append(np.mean(times) * 1e6)  # Convertir a µs

        # 📌 Medir Fuerza Bruta
        times = []
        for _ in range(num_trials):
            start_time = time.perf_counter()
            subsetSum_force(size, arr, x)
            times.append(time.perf_counter() - start_time)
        results["Fuerza Bruta"].append(np.mean(times) * 1e6)

        # 📌 Medir Programación Dinámica
        times = []
        for _ in range(num_trials):
            start_time = time.perf_counter()
            ProgramacionDP(arr, x)
            times.append(time.perf_counter() - start_time)
        results["Programación Dinámica"].append(np.mean(times) * 1e6)

        # 📌 Medir Backtracking
        times = []
        for _ in range(num_trials):
            start_time = time.perf_counter()
            encontrar_combinaciones(arr, x)
            times.append(time.perf_counter() - start_time)
        results["Backtracking"].append(np.mean(times) * 1e6)

    return results, sizes

# 🔹 Gráfica comparativa de curvas de complejidad
def plot_curves(results, sizes):
    plt.figure(figsize=(10, 6))

    for label, times in results.items():
        plt.plot(sizes, times, marker='o', linestyle='-', label=label)
    
    # 📌 Configuración del gráfico
    plt.xlabel("Tamaño del Conjunto (n)")
    plt.ylabel("Tiempo de Ejecución (µs)")
    plt.title("Comparación de Algoritmos: Complejidad Temporal")
    plt.yscale("log")  # 📌 Escala logarítmica para mejor visualización
    plt.xticks(sizes)
    plt.legend()
    plt.grid(True, linestyle="--", linewidth=0.5)
    plt.show()

# 🔹 Ejecutar prueba y graficar
if __name__ == "__main__":
    results, sizes = test_performance()
    plot_curves(results, sizes)
