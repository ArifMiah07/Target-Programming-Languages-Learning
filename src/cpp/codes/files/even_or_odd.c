#include<stdio.h>
int main()
{
    int number;
    printf("Enter a number: \n");
    scanf("%d", &number);
    if(number % 2 == 0){
        printf("%d is Even Number! \n", number);
    }else{
        printf("%d is odd Number! \n", number);
    }

    return 0;
}