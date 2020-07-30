#include <stdio.h>
#include <stdlib.h>

int main()
{
    // Code here
    
    /*
     * %c       - Character
     * %d       - Integer (base 10)
     * %e       - Exponential floating-point
     * %f       - Floating-point
     * %i       - Integer (base 10)
     * %o       - Octal (base 8)
     * %s       - String
     * %u       - Unsigned decimal (integer) number
     * %x       - Hexadecimal (base 16)
     * %%       - Print a percent sign
     * \%       - Print a percent sign
     */

    printf("Hello\nWorld\n"); // Function that prints stuff to STDOUT.
    printf("%d\n", 500); // Format specifier for a number. % calls a format specifier, and the letter is the format

    printf("My favorite %s is %d.\n", "number", 500);
    printf("My second favorite is %f.\n", 500.98754);

    int favNum = 90;
    printf("My third favorite is %d", favNum);
    return 0;
}
