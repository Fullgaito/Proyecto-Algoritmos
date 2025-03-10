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
<<<<<<< HEAD
=======

>>>>>>> c07709e3c63773c2ceced072eaabffd9a410b90d
arr = [93, 7, 15, 1, 35, 5, 21, 47, 3, 55, 17, 9, 75, 29, 13, 43, 19, 31, 23, 11]
x = 100
n=len(arr)
subsetSum(n, arr, x)
time_elapsed = (time.perf_counter() - time_start)

print(time_elapsed)