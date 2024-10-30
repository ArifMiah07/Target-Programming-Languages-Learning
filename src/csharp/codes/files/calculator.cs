using System;

class Calculator
{
    static void Main()
    {
        int sum;
        int avg;
        int num1, num2, num3;

        Console.WriteLine("Enter three numbers: ");
        num1 = Convert.ToInt32(Console.ReadLine());
        num2 = Convert.ToInt32(Console.ReadLine());
        num3 = Convert.ToInt32(Console.ReadLine());

        sum = num1 + num2 + num3;
        avg = sum / 3;

        Console.WriteLine("Average: " + avg);
    }
}

// power by chatgpt o| written by chatgpt o| copy from chatgpt