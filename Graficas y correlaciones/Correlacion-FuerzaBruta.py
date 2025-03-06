import time
import random
import json
import numpy as np
import matplotlib.pyplot as plt
from itertools import combinations
from scipy.optimize import curve_fit
from scipy.stats import linregress

def subsetSum(n, arr, x):
    """Busca subconjuntos cuya suma sea igual a x."""
    valid_combinations = []
    for i in range(n + 1):
        for subset in combinations(arr, i):
            if sum(subset) == x:
                valid_combinations.append(list(subset))  # Guardar combinación válida
    return valid_combinations

def test_performance():
    sizes = list(range(2, 25, 2))  # Tamaños de listas de prueba (de 2 a 24 en pasos de 2)
    times = []
    data = []

    for size in sizes:
        arr = [random.randint(1, 20) for _ in range(size)]  # Array de números aleatorios
        x = random.randint(5, 40)  # Valor objetivo aleatorio

        start_time = time.perf_counter()  # Iniciar medición de tiempo
        valid_combinations = subsetSum(size, arr, x)
        elapsed_time = time.perf_counter() - start_time  # Calcular tiempo transcurrido

        times.append(elapsed_time)  # Guardar el tiempo

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
    with open("datos_FuerzaBruta.json", "w") as f:
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