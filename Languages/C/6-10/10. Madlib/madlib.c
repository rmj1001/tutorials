#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void stripNewline(char *string)
{
    int new_line = strlen(string) -1;
    if (string[new_line] == '\n') {
        string[new_line] = '\0';
    }
}

int main()
{
    char color[50];
    char pluralNoun[50];
    char celebrity[50];

    printf("Enter a color: ");
    fgets(color, 50, stdin);

    printf("Enter a plural noun: ");
    fgets(pluralNoun, 50, stdin);
    
    printf("Enter a celebrity: ");
    fgets(celebrity, 50, stdin);

    stripNewline(color);
    stripNewline(pluralNoun);
    stripNewline(celebrity);

    printf("\n");
    printf("Roses are %s,\n", color);
    printf("%s are blue,\n", pluralNoun);
    printf("I love %s.\n", celebrity);
    return 0;
}
