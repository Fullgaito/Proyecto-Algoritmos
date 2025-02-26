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

def test_performance():
    """
    Prueba el rendimiento del algoritmo con diferentes tamaños de array.
    """
    sizes = list(range(2, 21, 2))  # Tamaños de 2 a 20 en pasos de 2
    times = []
    
    for size in sizes:
        # Generar array aleatorio y valor objetivo
        arr = sorted(random.sample(range(1, 100), size))
        M = random.randint(size*2, size*5)
        
        # Medir tiempo de ejecución
        tiempo_inicio = time.perf_counter()
        encontrar_combinaciones(arr.copy(), M)
        tiempo_total = time.perf_counter() - tiempo_inicio
        times.append(tiempo_total)
    
    return np.array(sizes), np.array(times)

def linear_model(x, a, b):
    """Modelo lineal: f(x) = ax + b"""
    return a * x + b

def exponential_model(x, a, b):
    """Modelo exponencial: f(x) = ae^(bx)"""
    return a * np.exp(b * x)

def polynomial_model(x, a, b, c):
    """Modelo polinómico: f(x) = ax^2 + bx + c"""
    return a * x**2 + b * x + c

def graph_and_fit():
    """
    Realiza el análisis de rendimiento y ajuste de curvas.
    """
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
    
    # Ajuste Polinómico
    popt_poly, _ = curve_fit(polynomial_model, sizes, times)
    times_pred_poly = polynomial_model(sizes, *popt_poly)
    r_poly = np.corrcoef(times, times_pred_poly)[0, 1]**2
    
    # Crear gráfico
    plt.figure(figsize=(10, 6))
    plt.scatter(sizes, times, color="blue", label="Datos Originales")
    
    # Graficar ajustes
    plt.plot(sizes, linear_model(sizes, *popt_linear), 
             label=f"Ajuste Lineal (R²={r_linear:.4f})", linestyle="--")
    plt.plot(sizes, polynomial_model(sizes, *popt_poly), 
             label=f"Ajuste Polinómico (R²={r_poly:.4f})", linestyle="-.")
    if r_exp > 0:
        plt.plot(sizes, exponential_model(sizes, *popt_exp), 
                 label=f"Ajuste Exponencial (R²={r_exp:.4f})", linestyle=":")
    
    plt.xlabel("Tamaño del Array")
    plt.ylabel("Tiempo de Ejecución (segundos)")
    plt.title("Análisis de Complejidad Temporal - Backtracking")
    plt.legend()
    plt.grid(True)
    plt.show()
    
    # Determinar mejor ajuste
    best_fit = max([("Lineal", r_linear), ("Exponencial", r_exp), 
                   ("Polinómico", r_poly)], key=lambda x: x[1])
    print(f"\nMejor ajuste: {best_fit[0]} con R² = {best_fit[1]:.4f}")

# Ejecutar el análisis
if __name__ == "__main__":
    graph_and_fit()