import time
import random
import json
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
    data = []
    
    for size in sizes:
        # Generar array aleatorio y valor objetivo
        arr = sorted(random.sample(range(1, 100), size))
        M = random.randint(size * 2, size * 5)
        
        # Medir tiempo de ejecución
        tiempo_inicio = time.perf_counter()
        soluciones = encontrar_combinaciones(arr.copy(), M)
        tiempo_total = time.perf_counter() - tiempo_inicio
        times.append(tiempo_total)
        
        # Verificar que las soluciones sean consistentes con el arreglo
        soluciones_validas = []
        for sol in soluciones:
            if all(num in arr for num in sol) and sum(sol) == M:
                soluciones_validas.append(sol)
        
        # Guardar datos en formato JSON
        caso = {
            "tamaño": size,
            "array": arr,
            "suma_objetivo": M,
            "soluciones": soluciones_validas,
            "tiempo_ejecucion": tiempo_total
        }
        data.append(caso)
    
    # Guardar datos en un archivo JSON
    with open("datos_Backtracking.json", "w") as f:
        json.dump(data, f, indent=4)
    
    return np.array(sizes), np.array(times)

def exponential_model(x, a, b):
    """Modelo exponencial: f(x) = ae^(bx)"""
    return a * np.exp(b * x)

def graph_and_fit():
    """
    Realiza el análisis de rendimiento y ajuste de curvas.
    """
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
    plt.title("Análisis de Complejidad Temporal - Backtracking")
    plt.legend()
    plt.grid(True)
    plt.show()
    
    # Determinar mejor ajuste
    print(f"\nMejor ajuste: Exponencial con R² = {r_exp:.4f}")

# Ejecutar el análisis
if __name__ == "__main__":
    graph_and_fit()