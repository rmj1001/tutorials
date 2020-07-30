#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void saysHi() {
    printf("Hello User! \n");
}

void saysBye(char name[]) {
    printf("Goodbye, %s. \n", name);
}

void echo(char string[]) {
    printf("%s \n", string);
}

int main()
{
    echo("Top");
    saysHi();
    echo("Bottom");
    saysBye("Kaleb");
    return 0;
}
