import time
import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.stats import linregress

# 🔹 Algoritmo por Backtracking
def encontrar_combinaciones(arr, M, index=0, suma_actual=0, combinacion=[], soluciones=[]):
    if suma_actual == M:
        soluciones.append(combinacion[:])  # Guardar copia de la combinación encontrada
        return
    
    if index >= len(arr) or suma_actual > M:
        return
    
    # Opción 1: Incluir arr[index] en la combinación
    encontrar_combinaciones(arr, M, index + 1, suma_actual + arr[index], combinacion + [arr[index]], soluciones)
    
    # Opción 2: No incluir arr[index] y pasar al siguiente
    encontrar_combinaciones(arr, M, index + 1, suma_actual, combinacion, soluciones)

    return soluciones

# 🔹 Prueba de rendimiento
def test_performance():
    sizes = list(range(2, 22, 2))  # Probamos tamaños de 2 a 22 elementos
    times = []

    for size in sizes:
        arr = [random.randint(1, 20) for _ in range(size)]
        x = random.randint(5, 40)

        start_time = time.perf_counter()
        encontrar_combinaciones(arr, x)
        elapsed_time = time.perf_counter() - start_time

        times.append(elapsed_time)

    return np.array(sizes), np.array(times)

# 🔹 Definimos funciones de ajuste
def exponential_model(x, a, b):
    return a * np.exp(b * x)

def polynomial_model(x, a, b, c):
    return a * x**2 + b * x + c

# 🔹 Graficar y encontrar mejor ajuste
def graph_and_fit():
    sizes, times = test_performance()

    # Ajuste Exponencial
    popt_exp, _ = curve_fit(exponential_model, sizes, times, maxfev=5000)
    times_pred_exp = exponential_model(sizes, *popt_exp)
    r_exp = np.corrcoef(times, times_pred_exp)[0, 1]**2

    # Ajuste Polinómico de 2do grado
    popt_poly, _ = curve_fit(polynomial_model, sizes, times)
    times_pred_poly = polynomial_model(sizes, *popt_poly)
    r_poly = np.corrcoef(times, times_pred_poly)[0, 1]**2

    # 📊 Graficamos los puntos originales
    plt.figure(figsize=(10, 6))
    plt.scatter(sizes, times, color="red", label="Datos Originales")

    # 📈 Graficamos cada ajuste
    plt.plot(sizes, exponential_model(sizes, *popt_exp), label=f"Ajuste Exponencial (R²={r_exp:.4f})", linestyle="--")
    plt.plot(sizes, polynomial_model(sizes, *popt_poly), label=f"Ajuste Polinómico (R²={r_poly:.4f})", linestyle="--")

    plt.xlabel("Tamaño del Array")
    plt.ylabel("Tiempo de Ejecución (segundos)")
    plt.title("Análisis de Complejidad del Algoritmo Backtracking")
    plt.legend()
    plt.grid(True)
    plt.show()

    # 🔹 Determinar mejor ajuste
    best_fit = max([("Exponencial", r_exp), ("Polinómico", r_poly)], key=lambda x: x[1])
    print(f"🔹 Mejor ajuste: {best_fit[0]} con R² = {best_fit[1]:.4f}")

# 🔹 Ejecutar la prueba y graficar
if __name__ == "__main__":
    graph_and_fit()
