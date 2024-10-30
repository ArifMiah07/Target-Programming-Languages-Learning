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

    printf("sum: %d\n", sum);
    printf("avg: %d\n", avg);
    return 0;
}

//advance

// #include <stdio.h>
// #include <stdlib.h>
// #include <stdbool.h>

// bool isValidInteger(char *str) {
//     // Check if the input string is a valid integer
//     if (*str == '-' || *str == '+') str++;  // Allow a leading sign

//     // Ensure all characters are digits
//     while (*str) {
//         if (!(*str >= '0' && *str <= '9')) return false;
//         str++;
//     }
//     return true;
// }

// int main() {
//     int num1, num2, num3;
//     int sum, avg;
//     char input1[100], input2[100], input3[100];

//     printf("Enter three numbers separated by spaces: \n");

//     // Scan inputs as strings for validation
//     if (scanf("%s %s %s", input1, input2, input3) != 3) {
//         printf("Error: Please enter exactly three numbers.\n");
//         return 1;
//     }

//     // Validate each input as an integer
//     if (!isValidInteger(input1) || !isValidInteger(input2) || !isValidInteger(input3)) {
//         printf("Error: All inputs must be valid integers.\n");
//         return 1;
//     }

//     // Convert validated strings to integers
//     num1 = atoi(input1);
//     num2 = atoi(input2);
//     num3 = atoi(input3);

//     // Calculate sum and average
//     sum = num1 + num2 + num3;
//     avg = sum / 3;

//     printf("Sum: %d\n", sum);
//     printf("Average: %d\n", avg);

//     return 0;
// }
