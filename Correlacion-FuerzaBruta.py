import time
import random
import numpy as np
import matplotlib.pyplot as plt
from itertools import combinations
from scipy.optimize import curve_fit
from scipy.stats import linregress

def subsetSum(n, arr, x):
    """Busca subconjuntos cuya suma sea igual a x."""
    for i in range(n + 1):
        for subset in combinations(arr, i):
            if sum(subset) == x:
                pass  # Simplemente verificamos, no imprimimos para ahorrar tiempo

# 🔹 Prueba de rendimiento
def test_performance():
    sizes = list(range(2, 25, 2))  # Tamaños de listas de prueba (de 2 a 20 en pasos de 2)
    times = []

    for size in sizes:
        arr = [random.randint(1, 20) for _ in range(size)]  # Array de números aleatorios
        x = random.randint(5, 40)  # Valor objetivo aleatorio

        start_time = time.perf_counter()  # Iniciar medición de tiempo
        subsetSum(size, arr, x)
        elapsed_time = time.perf_counter() - start_time  # Calcular tiempo transcurrido

        times.append(elapsed_time)  # Guardar el tiempo

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
    r_linear = linregress(sizes, times).rvalue**2  # Coeficiente de correlación R^2

    # Ajuste Exponencial
    try:
        popt_exp, _ = curve_fit(exponential_model, sizes, times, maxfev=5000)
        times_pred_exp = exponential_model(sizes, *popt_exp)
        r_exp = np.corrcoef(times, times_pred_exp)[0, 1]**2
    except RuntimeError:
        r_exp = 0  # Si el ajuste falla, asignamos 0

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
    plt.title("Ajuste de Función a la Complejidad del Algoritmo")
    plt.legend()
    plt.grid(True)
    plt.show()  # Mostrar la gráfica

    # 🔹 Determinar cuál ajuste es mejor
    best_fit = max([("Lineal", r_linear), ("Exponencial", r_exp), ("Polinómico", r_poly)], key=lambda x: x[1])
    print(f"🔹 Mejor ajuste: {best_fit[0]} con R² = {best_fit[1]:.4f}")

# 🔹 Ejecutar la prueba y graficar
if __name__ == "__main__":
    graph_and_fit()