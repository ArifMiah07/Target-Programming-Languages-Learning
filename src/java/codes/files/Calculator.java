import java.util.Scanner;

public class Calculator { // This should match the filename if public
    public static void main(String[] args) {
        int sum;
        int avg;
        int num1, num2, num3;

        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter three numbers: ");
        num1 = scanner.nextInt();
        num2 = scanner.nextInt();
        num3 = scanner.nextInt();

        sum = num1 + num2 + num3;
        avg = sum / 3;

        System.out.println("avg: " + avg);

        scanner.close();
    }
}


//power by chatgpt o| copy from Chatgpt