#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void encontrar_combinaciones(int *arr, int n, int M, int index, int suma_actual, int *combinacion, int combinacion_len)
{
    if (suma_actual == M)
    {
        printf("[");
        for (int i = 0; i < combinacion_len; i++)
        {
            printf("%d%s", combinacion[i], (i < combinacion_len - 1) ? ", " : "");
        }
        printf("]\n");
        return;
    }
    
    if (index >= n || suma_actual > M)
        return;

    // Opción 1: Incluir arr[index] en la combinación
    combinacion[combinacion_len] = arr[index];
    encontrar_combinaciones(arr, n, M, index + 1, suma_actual + arr[index], combinacion, combinacion_len + 1);

    // Opción 2: No incluir arr[index] y pasar al siguiente
    encontrar_combinaciones(arr, n, M, index + 1, suma_actual, combinacion, combinacion_len);
}

int main()
{
    clock_t inicio = clock();
    
    int conjunto[] = {2, 4, 8, 6, 10};
    int M = 10;
    int n = sizeof(conjunto) / sizeof(conjunto[0]);
    int *combinacion = (int *)malloc(n * sizeof(int));
    
    encontrar_combinaciones(conjunto, n, M, 0, 0, combinacion, 0);
    
    free(combinacion);
    clock_t fin = clock();
    printf("Tiempo de ejecuci\xC3\xB3n: %lf segundos\n", (double)(fin - inicio) / CLOCKS_PER_SEC);
    
    return 0;
}
