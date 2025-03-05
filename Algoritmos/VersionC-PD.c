#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void ProgramacionDP(int *arr, int n, int m)
{
	int i = 0;
	int j = 0; 
    int ***dp = (int ***)malloc((m + 1) * sizeof(int **));
    for (i = 0; i <= m; i++)
    {
        dp[i] = (int **)malloc(n * sizeof(int *));
        for (int j = 0; j < n; j++)
            dp[i][j] = NULL;
    }
    
    dp[0][0] = (int *)malloc(sizeof(int)); // Caso base
    dp[0][0][0] = 0;
    
    for (int i = 0; i < n; i++)
    {
        for (int j = m; j >= arr[i]; j--)
        {
            if (dp[j - arr[i]][0] != NULL)
            {
                dp[j][0] = (int *)malloc(sizeof(int) * (i + 1));
                for (int k = 0; k < i; k++)
                    dp[j][0][k] = dp[j - arr[i]][0][k];
                dp[j][0][i] = arr[i];
            }
        }
    }
    
    if (dp[m][0] != NULL)
    {
        printf("Combinaciones que suman %d: [", m);
        for (int i = 0; i < n && dp[m][0][i] != 0; i++)
            printf("%d%s", dp[m][0][i], (dp[m][0][i + 1] != 0) ? ", " : "");
        printf("]\n");
    }
    else
        printf("No hay combinaciones que sumen %d\n", m);
    
    for (int i = 0; i <= m; i++)
        free(dp[i]);
    free(dp);
}

int main()
{
    clock_t start = clock();
    
    int arr[] = {2, 4, 8, 6, 10};
    int m = 10;
    int n = sizeof(arr) / sizeof(arr[0]);
    
    ProgramacionDP(arr, n, m);
    
    clock_t end = clock();
    printf("Tiempo transcurrido: %lf segundos\n", (double)(end - start) / CLOCKS_PER_SEC);
    
    return 0;
}