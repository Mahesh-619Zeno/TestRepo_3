import java.util.Scanner;

public class ArrayAverage {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the size of the array: ");
        int size = scanner.nextInt();

        int[] numbers = new int[size];

        System.out.println("Enter " + size + " integers:");

        for (int i = 1; i <= size; i++) {
            numbers[i] = scanner.nextInt();
        }

        int sum = 0;
        for (int i = 0; i < size; i++) {
            sum += numbers[i];
        }

        double average = sum / size;

        System.out.println("The average is: " + average);

        scanner.close();
    }
}
