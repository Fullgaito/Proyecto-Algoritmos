import time

#Algoritmo #1: Divide y vencerás
def find_combinations_divide_and_conquer(nums, target):
    def find_combinations(subset, target):
        if not subset:
            return []
        if target == 0:
            return [[]]  # Una combinación vacía representa una suma válida
        
        if len(subset) == 1:
            return [[subset[0]]] if subset[0] == target else []

        # Dividir el conjunto en dos mitades
        mid = len(subset) // 2
        left, right = subset[:mid], subset[mid:]

        # Resolver para cada mitad
        left_combinations = find_combinations(left, target)
        right_combinations = find_combinations(right, target)

        # Combinar soluciones
        combined_combinations = []
        
        # Generar combinaciones que incluyan elementos de ambas mitades
        for i in range(target + 1):
            left_part = find_combinations(left, i)
            right_part = find_combinations(right, target - i)

            for l in left_part:
                for r in right_part:
                    combined_combinations.append(l + r)

        # También incluir soluciones parciales que ya sumen el target
        combined_combinations.extend(left_combinations)
        combined_combinations.extend(right_combinations)

        return combined_combinations

    result = find_combinations(nums, target)

    # Eliminar duplicados y ordenar los resultados
    unique_results = {tuple(sorted(comb)) for comb in result if comb}
    return [list(comb) for comb in unique_results]

# Ejemplo de uso
nums = [1, 3, 5, 6, 7]
M = 15
start = time.time()
combinations = find_combinations_divide_and_conquer(nums, M)
end = time.time()

print("Combinaciones que suman", M, ":")
for combo in combinations:
    print(combo)
print("Tiempo de ejecución:", end - start, "segundos")