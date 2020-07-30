#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main()
{
    // Code here
    
    printf("%f\n", 8.9); // %f is a placeholder for a floating point number
    printf("%f\n", 5.0 + 4.5);
    printf("%f\n", 5.0 * 4.5);
    
    // Floating point numbers must have at least one decimal.
    printf("%d\n", 5 - 4); // %d supports integers
    
    int num = 6;
    printf("%d\n", num);
    printf("%f\n", pow(2, 3));

    return 0;
}
