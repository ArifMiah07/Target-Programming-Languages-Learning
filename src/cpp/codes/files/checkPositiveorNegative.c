#include<stdio.h>
int main()
{
    float n;
    printf("Enter a number: \n");
    scanf("%f", &n);
    if( n < 0){
        printf("%f is a negative number: \n", n);
    }else if ( n == 0){
        printf("%f is zero: \n", n);
    }else{
        printf("%f is a positive number: \n", n);
    }

    return 0;
}