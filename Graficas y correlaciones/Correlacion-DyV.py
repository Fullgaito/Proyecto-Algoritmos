import time
import random
import json
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.stats import linregress

def subsetSum(arr, index, current_subset, comb_list, sum_list):
    """Genera todas las combinaciones posibles de subconjuntos y sus sumas."""
    if index == len(arr):
        comb_list.append(current_subset[:])  # Copia del subconjunto actual
        sum_list.append(sum(current_subset))
        return

    # Incluir el elemento actual
    current_subset.append(arr[index])
    subsetSum(arr, index + 1, current_subset, comb_list, sum_list)

    # Excluir el elemento actual
    current_subset.pop()
    subsetSum(arr, index + 1, current_subset, comb_list, sum_list)

def calcSubsets(n, arr, x):
    """Divide el array en dos partes, genera los subconjuntos y busca combinaciones cuya suma sea x."""
    arr1, arr2 = arr[:n // 2], arr[n // 2:]

    # Obtener subconjuntos y sumas para cada mitad
    comb1, sums1 = [], []
    subsetSum(arr1, 0, [], comb1, sums1)

    comb2, sums2 = [], []
    subsetSum(arr2, 0, [], comb2, sums2)

    # Buscar combinaciones cuya suma sea x
    valid_combinations = []
    for i in range(len(sums1)):
        for j in range(len(sums2)):
            if sums1[i] + sums2[j] == x:
                valid_combinations.append(comb1[i] + comb2[j])

    return valid_combinations

def test_performance():
    sizes = list(range(2, 30, 2))  # Tamaños de listas de prueba (de 2 a 30 en pasos de 2)
    times = []
    data = []

    for size in sizes:
        arr = [random.randint(1, 20) for _ in range(size)]
        x = random.randint(5, 40)

        start_time = time.perf_counter()
        valid_combinations = calcSubsets(size, arr, x)
        elapsed_time = time.perf_counter() - start_time

        times.append(elapsed_time)

        # Guardar datos en formato JSON
        caso = {
            "tamaño": size,
            "array": arr,
            "suma_objetivo": x,
            "soluciones": valid_combinations,
            "tiempo_ejecucion": elapsed_time
        }
        data.append(caso)

    # Guardar datos en un archivo JSON
    with open("datos_DyV.json", "w") as f:
        json.dump(data, f, indent=4)

    return np.array(sizes), np.array(times)

def exponential_model(x, a, b):
    """Modelo exponencial: f(x) = ae^(bx)"""
    return a * np.exp(b * x)

def graph_and_fit():
    sizes, times = test_performance()

    # Ajuste Exponencial
    try:
        popt_exp, _ = curve_fit(exponential_model, sizes, times, maxfev=5000)
        times_pred_exp = exponential_model(sizes, *popt_exp)
        r_exp = np.corrcoef(times, times_pred_exp)[0, 1]**2
    except RuntimeError:
        r_exp = 0
        popt_exp = (0, 0)

    # Crear gráfico
    plt.figure(figsize=(10, 6))
    plt.scatter(sizes, times, color="blue", label="Datos Originales")

    # Graficar ajuste exponencial
    plt.plot(sizes, exponential_model(sizes, *popt_exp), 
             label=f"Ajuste Exponencial (R²={r_exp:.4f})", linestyle="--")

    plt.xlabel("Tamaño del Array")
    plt.ylabel("Tiempo de Ejecución (segundos)")
    plt.title("Análisis de Complejidad Temporal - Subset Sum")
    plt.legend()
    plt.grid(True)
    plt.show()

    # Determinar mejor ajuste
    print(f"\nMejor ajuste: Exponencial con R² = {r_exp:.4f}")

# Ejecutar el análisis
if __name__ == "__main__":
    graph_and_fit()