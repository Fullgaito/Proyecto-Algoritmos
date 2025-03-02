import time
import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# 🔹 Algoritmo de Programación Dinámica
def ProgramacionDP(n, m):
    """Encuentra todas las combinaciones de n que suman m usando programación dinámica."""
    dp = [[] for _ in range(m + 1)]
    dp[0] = [[]]  # Caso base: suma 0 tiene una combinación vacía

    for num in n:
        for j in range(m, num - 1, -1):
            for prev in dp[j - num]:
                dp[j].append(prev + [num])

    return dp[m]

# 🔹 Prueba de rendimiento
def test_performance():
    """Mide el tiempo de ejecución para diferentes tamaños de `n` y valores `m`."""
    sizes = list(range(2, 100, 2))  # Tamaños de prueba (de 2 a 30 en pasos de 2)
    times = []

    for size in sizes:
        total_time = 0
        num_trials = 10  # Más mediciones para mayor precisión

        for _ in range(num_trials):
            n = [random.randint(1, 20) for _ in range(size)]
            m = random.randint(5, 40)

            start_time = time.perf_counter()
            ProgramacionDP(n, m)
            elapsed_time = time.perf_counter() - start_time
            total_time += elapsed_time

        avg_time = (total_time / num_trials) * 1e6  # Convertimos a microsegundos
        times.append(avg_time)

    return np.array(sizes), np.array(times)

# 🔹 Graficar los resultados y calcular correlación
def graph_results():
    """
    Genera la gráfica de dispersión con la correlación correcta.
    """
    sizes, times = test_performance()

    # 📌 Aplicar logaritmo a los tiempos para mejorar la regresión
    log_times = np.log10(times)  # Transformamos a escala logarítmica base 10

    # 📌 Calcular coeficiente de correlación con `scipy.stats.linregress`
    slope, intercept, r_value, _, _ = linregress(sizes, log_times)
    r2 = r_value**2  # R² de la regresión logarítmica

    plt.figure(figsize=(8, 6))

    # 📊 Gráfica: Tiempo vs Tamaño del Conjunto con escala logarítmica
    plt.scatter(sizes, times, color="red", label="Datos Originales")

    # 📌 Graficamos la regresión pero revirtiendo la transformación logarítmica
    regression_line = 10**(intercept + slope * sizes)  # Volvemos a la escala original
    plt.plot(sizes, regression_line, color="blue", linestyle="--", label=f"Regresión (R² = {r2:.4f})")

    plt.xlabel("Tamaño del Conjunto (n)")
    plt.ylabel("Tiempo de Ejecución (μs)")
    plt.yscale("log")  # Escala logarítmica para una mejor visualización
    plt.title("Tiempo vs Tamaño del Conjunto (Programación Dinámica)")
    plt.legend()
    plt.grid(True, which="both", linestyle="--", linewidth=0.5)

    plt.show()

    # 🔹 Mostrar correlación en consola
    print(f"🔹 Correlación Tiempo vs Tamaño del Conjunto: R² = {r2:.4f}")

# 🔹 Ejecutar la prueba y graficar
if __name__ == "__main__":
    graph_results()
