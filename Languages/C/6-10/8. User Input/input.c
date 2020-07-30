#include <stdio.h>
#include <stdlib.h>

int main()
{
    char name[20];
    int age;
    double gpa;
    char grade;

    // Prompt the user first
    printf("Enter your name: ");
    fgets(name, 20, stdin);
    
    printf("Enter your age: ");
    scanf("%d", &age);
    
    printf("Enter your grade: ");
    scanf(" %c", &grade); // Stops skipping bc it doesn't take the newline char as a character.
    
    printf("Enter your gpa: ");
    scanf("%lf", &gpa);
  
    printf("\n\nName: %s", name);
    printf("Age: %d\n", age);
    printf("GPA: %f\n", gpa);
    printf("Grade: %c\n", grade);
    return 0;
}
