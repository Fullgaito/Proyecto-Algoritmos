#complejidad temporal O(2^n)
#complejidad espacial O(2^n)

import time
time_start = time.perf_counter()
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
    for i in range(len(sums1)):
        for j in range(len(sums2)):
            if sums1[i] + sums2[j] == x:
                print(comb1[i] + comb2[j])

# Prueba del algoritmo

<<<<<<< HEAD
arr = [93, 7, 15, 1, 35, 5, 21, 47, 3, 55, 17, 9, 75, 29, 13, 43, 19, 31, 23, 11]
=======
arr = [93,7,15,1,35,5,21,47,3,55,17,9,75,29,13,43,19,31,23,11]
>>>>>>> c07709e3c63773c2ceced072eaabffd9a410b90d
x = 100
n=len(arr)
calcSubsets(n, arr, x)


time_elapsed = (time.perf_counter() - time_start)

print(time_elapsed)