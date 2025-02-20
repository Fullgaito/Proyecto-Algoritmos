from itertools import combinations
import timeit

def fuerza_bruta(nums, M):
    result = []
    for r in range(1, len(nums) + 1):
        for combo in combinations(nums, r):
            if sum(combo) == M:
                result.append(combo)
    return result

lista=[2,4,8,6,10]
M=10

start_time = timeit.timeit()
solucion=fuerza_bruta(lista,M)
end_time = timeit.timeit()

print(solucion,round(start_time-end_time,8))



