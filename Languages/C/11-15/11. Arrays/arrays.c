#include <stdio.h>
#include <stdlib.h>

int main()
{
    int luckyNumbers[] = {4, 8, 15, 16, 23, 42};
    printf("%d\n", luckyNumbers[0]);

    // Modify array
    int before = luckyNumbers[1];
    luckyNumbers[1] = 200;
    printf("Before: %d\nAfter: %d\n", before, luckyNumbers[1]);

    // Initialize array before definition
    int newNumbers[10]; // If not defining the array, you must allocate space to it.
    
    newNumbers[0] = 1;
    newNumbers[1] = 2;
    printf("%d, %d\n", newNumbers[0], newNumbers[1]);

    return 0;
}