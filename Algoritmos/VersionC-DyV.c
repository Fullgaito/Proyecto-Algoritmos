#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void subsetSum(int *arr, int index, int *currentSubset, int currentSize, int **combList, int *combSizes, int *sumList, int *combCount)
{
    if (index == currentSize)
    {
        int i;
        combList[*combCount] = (int *)malloc(currentSize * sizeof(int));
        for (i = 0; i < currentSize; i++)
        {
            combList[*combCount][i] = currentSubset[i];
        }
        combSizes[*combCount] = currentSize;
        sumList[*combCount] = 0;
        for (i = 0; i < currentSize; i++)
        {
            sumList[*combCount] += currentSubset[i];
        }
        (*combCount)++;
        return;
    }

    // Incluir el elemento actual
    currentSubset[currentSize] = arr[index];
    subsetSum(arr, index + 1, currentSubset, currentSize + 1, combList, combSizes, sumList, combCount);

    // Excluir el elemento actual
    subsetSum(arr, index + 1, currentSubset, currentSize, combList, combSizes, sumList, combCount);
}

void calcSubsets(int n, int *arr, int x)
{
    int i, j, k;
    int mid = n / 2;
    int *arr1 = arr;
    int *arr2 = arr + mid;
    int size1 = mid, size2 = n - mid;

    int **comb1 = (int **)malloc((1 << size1) * sizeof(int *));
    int *combSizes1 = (int *)malloc((1 << size1) * sizeof(int));
    int *sums1 = (int *)malloc((1 << size1) * sizeof(int));
    int count1 = 0;
    int *tempSubset = (int *)malloc(size1 * sizeof(int));
    
    subsetSum(arr1, 0, tempSubset, 0, comb1, combSizes1, sums1, &count1);
    free(tempSubset);

    int **comb2 = (int **)malloc((1 << size2) * sizeof(int *));
    int *combSizes2 = (int *)malloc((1 << size2) * sizeof(int));
    int *sums2 = (int *)malloc((1 << size2) * sizeof(int));
    int count2 = 0;
    tempSubset = (int *)malloc(size2 * sizeof(int));
    
    subsetSum(arr2, 0, tempSubset, 0, comb2, combSizes2, sums2, &count2);
    free(tempSubset);

    for (i = 0; i < count1; i++)
    {
        int sum1 = sums1[i];
        int size1 = combSizes1[i];
        for (j = 0; j < count2; j++)
        {
            int sum2 = sums2[j];
            int size2 = combSizes2[j];
            if (sum1 + sum2 == x)
            {
                printf("[");
                for (k = 0; k < size1; k++)
                {
                    printf("%d", comb1[i][k]);
                    if (k < size1 - 1) printf(", ");
                }
                if (size1 > 0 && size2 > 0) printf(", ");
                for (k = 0; k < size2; k++)
                {
                    printf("%d", comb2[j][k]);
                    if (k < size2 - 1) printf(", ");
                }
                printf("]\n");
            }
        }
    }

    for (i = 0; i < count1; i++)
        free(comb1[i]);
    for (i = 0; i < count2; i++)
        free(comb2[i]);
    free(comb1);
    free(combSizes1);
    free(sums1);
    free(comb2);
    free(combSizes2);
    free(sums2);
}

int main()
{
    clock_t start = clock();

    int arr[] = {2, 4, 8, 6, 10};
    int x = 10;
    int n = sizeof(arr) / sizeof(arr[0]);

    calcSubsets(n, arr, x);

    clock_t end = clock();
    printf("Tiempo transcurrido: %lf segundos\n", (double)(end - start) / CLOCKS_PER_SEC);

    return 0;
}