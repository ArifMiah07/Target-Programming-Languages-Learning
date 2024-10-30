#include<stdio.h>
#include<math.h>

int main()
{
    int sum;
    int avg;
    int num1, num2, num3;

    printf("Enter three numbers: \n");
    scanf("%d %d %d", &num1, &num2, &num3);

    sum = num1 + num2 + num3;
    avg = sum / 3;

    printf("avg: %d\n", avg);
    return 0;
}