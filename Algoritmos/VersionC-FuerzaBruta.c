#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void generateSubsets(int *arr, int n, int x)
{
    int totalSubsets = 1 << n; // 2^n subconjuntos
    int i, j;
    
    for (i = 0; i < totalSubsets; i++)
    {
        int sum = 0;
        int first = 1;
        printf("[");
        
        for (j = 0; j < n; j++)
        {
            if (i & (1 << j)) // Verifica si el j-ésimo bit está activado
            {
                if (!first)
                    printf(", ");
                printf("%d", arr[j]);
                sum += arr[j];
                first = 0;
            }
        }
        
        printf("]");
        if (sum == x)
            printf(" <- Suma %d encontrada", x);
        printf("\n");
    }
}

int main()
{
    clock_t start, end;
    start = clock();

    int arr[] = {2, 4, 8, 6, 10};
    int x = 10;
    int n = sizeof(arr) / sizeof(arr[0]);

    generateSubsets(arr, n, x);

    end = clock();
    printf("Tiempo transcurrido: %lf segundos\n", (double)(end - start) / CLOCKS_PER_SEC);

    return 0;
}