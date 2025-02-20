import timeit

def ProgramacionDP(nums, M):
    # dp[i] almacenará todas las combinaciones que suman i
    dp = [[] for _ in range(M + 1)]
    dp[0] = [[]]  # Caso base: suma 0 tiene una combinación vacía

    # Iterar sobre cada número en el conjunto
    for num in nums:
        for j in range(M, num - 1, -1):
            for prev in dp[j - num]:
                dp[j].append(prev + [num])

    return dp[M]

# Prueba
nums = [2,4,8,6,10]
M = 10

start_time = timeit.timeit()
result = ProgramacionDP(nums, M)
end_time = timeit.timeit()

print(f"Programacion Dinamica - Combinaciones: {result}")
print(f"Tiempo de ejecucion: {end_time - start_time}")