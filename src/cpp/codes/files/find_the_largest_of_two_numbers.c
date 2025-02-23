#include<stdio.h>
int main()
{
    double num1, num2;
    printf("Enter tow number: \n");
    scanf("%lf %lf", &num1, &num2);
    if(num1 < num2){
        printf("%lf is the largest number. \n", num2);
    }else{
        printf("%lf is the largest number. \n", num1);
    }
    return 0;
}