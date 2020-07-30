#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int rawInput() {

    fflush(stdout);

    char input[50];
    char *fields;
    char symbol;
    double n1, n2, output;

    printf("Enter your equation.\n");
    printf("> ");
    scanf("%[^\n]", input);

    printf("\n%s", input);

    fields = strtok(input, " ");
    symbol = fields[1];
    n1 = (double)fields[0];
    n2 = (double)fields[2];

    switch (symbol) {
        case '+':
            output = n1 + n2;
            break;
        case '-':
            output = n1 - n2;
            break;
        case '*':
            output = n1 * n2;
            break;
        case '/':
            output = n1 / (float)n2;
            break;
        default:
            printf("Invalid operation!\n");
            return 1;
    }

    printf("Output: %f", output);
    return 0;
}

int calcMenu() {
    int choice;
    double n1, n2;
    double output;

    printf("Calculator\n\n");
    printf("1. Add\n");
    printf("2. Subtract\n");
    printf("3. Multiply\n");
    printf("4. Divide\n\n");
    printf("> ");
    scanf("%d", &choice);

    printf("\n");
    printf("First Number: ");
    scanf(" %lf", &n1);

    printf("Second Number: ");
    scanf(" %lf", &n2);

    switch(choice) {
        case 1:
            output = n1 + n2;
            break;
        case 2:
            output = n1 - n2;
            break;
        case 3:
            output = n1 * n2;
            break;
        case 4:
            output = n1 / (float)n2;
            break;
        default:
            printf("\n");
            printf("Invalid choice!\n");
            return 1;
    }

    printf("\n");
    printf("Your output is %f.\n", output);
    return 0;
}

int main()
{
    int menu;

    printf("Menu\n\n");
    printf("1. Raw Input\n");
    printf("2. Function Menu\n\n");
    printf("> ");
    scanf("%d", &menu);

    switch(menu) {
        case 1:
            rawInput();
            break;
        case 2:
            calcMenu();
            break;
        default:
            printf("Invalid input!\n");
            return 1;
    }
}