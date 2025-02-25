import time
import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.stats import linregress

def subsetSumDP(arr, target):
    """Encuentra subconjuntos cuya suma sea igual a 'target' usando Programación Dinámica."""
    dp = [[] for _ in range(target + 1)]
    dp[0] = [[]]  # La suma 0 tiene una combinación vacía

    for num in arr:
        for j in range(target, num - 1, -1):  
            for prev in dp[j - num]:
                dp[j].append(prev + [num])

    return len(dp[target]) > 0  # Retorna True si hay combinaciones para la suma 'target'

# 🔹 Prueba de rendimiento
def test_performance():
    sizes = list(range(2, 30, 2))  # Tamaños de listas de prueba (de 2 a 30 en pasos de 2)
    times = []

    for size in sizes:
        arr = [random.randint(1, 20) for _ in range(size)]
        x = random.randint(5, 40)

        start_time = time.perf_counter()
        subsetSumDP(arr, x)
        elapsed_time = time.perf_counter() - start_time

        times.append(elapsed_time)

    return np.array(sizes), np.array(times)

# 🔹 Definimos funciones de ajuste
def linear_model(x, a, b):
    return a * x + b

def exponential_model(x, a, b):
    return a * np.exp(b * x)

def polynomial_model(x, a, b, c):
    return a * x**2 + b * x + c

# 🔹 Graficar y encontrar mejor ajuste
def graph_and_fit():
    sizes, times = test_performance()

    # Ajuste Lineal
    popt_linear, _ = curve_fit(linear_model, sizes, times)
    r_linear = linregress(sizes, times).rvalue**2  

    # Ajuste Exponencial
    try:
        popt_exp, _ = curve_fit(exponential_model, sizes, times, maxfev=5000)
        times_pred_exp = exponential_model(sizes, *popt_exp)
        r_exp = np.corrcoef(times, times_pred_exp)[0, 1]**2
    except RuntimeError:
        r_exp = 0  

    # Ajuste Polinómico de 2do grado
    popt_poly, _ = curve_fit(polynomial_model, sizes, times)
    times_pred_poly = polynomial_model(sizes, *popt_poly)
    r_poly = np.corrcoef(times, times_pred_poly)[0, 1]**2

    # 📊 Graficamos los puntos originales
    plt.figure(figsize=(10, 6))
    plt.scatter(sizes, times, color="red", label="Datos Originales")

    # 📈 Graficamos cada ajuste
    plt.plot(sizes, linear_model(sizes, *popt_linear), label=f"Ajuste Lineal (R²={r_linear:.4f})", linestyle="--")
    plt.plot(sizes, polynomial_model(sizes, *popt_poly), label=f"Ajuste Polinómico (R²={r_poly:.4f})", linestyle="--")
    if r_exp > 0:
        plt.plot(sizes, exponential_model(sizes, *popt_exp), label=f"Ajuste Exponencial (R²={r_exp:.4f})", linestyle="--")

    plt.xlabel("Tamaño del Array")
    plt.ylabel("Tiempo de Ejecución (segundos)")
    plt.title("Ajuste de Función a la Complejidad del Algoritmo (DP)")
    plt.legend()
    plt.grid(True)
    plt.show()

    # 🔹 Determinar cuál ajuste es mejor
    best_fit = max([("Lineal", r_linear), ("Exponencial", r_exp), ("Polinómico", r_poly)], key=lambda x: x[1])
    print(f"🔹 Mejor ajuste: {best_fit[0]} con R² = {best_fit[1]:.4f}")

# 🔹 Ejecutar la prueba y graficar
if __name__ == "__main__":
    graph_and_fit()
