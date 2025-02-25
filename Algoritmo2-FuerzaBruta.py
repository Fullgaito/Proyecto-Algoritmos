#complejidad temporal O(n*2^n)
#complejidad espacial O(2^n)

import time

time_start = time.perf_counter()
# Python code with time complexity
# O(2^n)to print all subsets whose
# sum is equal to a given value
from itertools import combinations


def subsetSum(n, arr, x):
    # Iterating through all possible
    # subsets of arr from lengths 0 to n:
    for i in range(n + 1):
        for subset in combinations(arr, i):

            # printing the subset if its sum is x:
            if sum(subset) == x:
                print(list(subset))
    print("[" + "]")

# Driver Code:

arr = [2,4,8,6,10]
x = 10
n=len(arr)
subsetSum(n, arr, x)
time_elapsed = (time.perf_counter() - time_start)

print(time_elapsed)