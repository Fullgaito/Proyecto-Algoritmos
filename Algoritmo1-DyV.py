#Algoritmo 1: por divide y venceras
def encontrar_combinaciones(arr, M, index=0, suma_actual=0, combinacion=[]):
    if suma_actual == M:
        print(combinacion)  # Se encontró una combinación
        return
    
    if index >= len(arr) or suma_actual > M:
        return
    
    # Opción 1: Incluir arr[index] en la combinación
    encontrar_combinaciones(arr, M, index + 1, suma_actual + arr[index], combinacion + [arr[index]])
    
    # Opción 2: No incluir arr[index] y pasar al siguiente
    encontrar_combinaciones(arr, M, index + 1, suma_actual, combinacion)

# Ejemplo de uso
conjunto = [1, 3, 5, 6, 7]
M = 15
encontrar_combinaciones(conjunto, M)
