#include <stdio.h>
#include <stdlib.h>

int main()
{

    // Strings must use the `char var[] = "";` convention,
    // since they are just character arrays.
    char characterName[] = "John";
    int characterAge = 35;

    // Without variables
    printf("Without variables:\n");
    printf("There once was a man named George,\n");
    printf("he was 70 years old.\n");
    printf("He really liked the name George,\n");
    printf("but did not like being 70.\n");
    
    printf("\n\n");

    // With variables
    printf("With variables:\n");
    printf("There once was a man named %s,\n", characterName);
    printf("He was %d years old.\n", characterAge);

    // You can modify a variable later on
    characterAge = 60;
    
    printf("He really liked the name %s,\n", characterName);
    printf("But he did not like being %d.\n", characterAge);

    /*
    Variable Placeholder Types:
    
    %s, Character/String
    %d, Integer
    */
    return 0;
}