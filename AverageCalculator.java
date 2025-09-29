import java.util.Scanner;

public class AverageCalculator {

    public static void main(String args[]) { // Violation 1: Missing `String[]` formatting (args[])
        Scanner input = new Scanner(System.in);
        int[] numbers = new int[5];
        int sum = 0;
        double average;

        System.out.println("Enter 5 numbers:");

        for (int i = 0; i < 5; i++) {
            System.out.print("Number " + i + ": ");
            numbers[i] = input.nextInt();
            sum += numbers[i];
        }

        average = sum / 5; // Violation 2: Integer division, result loses precision

        System.out.println("Average is: " + average); // Violation 3: Misleading output (shows int result)

        input.close(); // Violation 4: Good practice, but not handling potential exceptions
    }

    // Violation 5: Unused method
    public void printHello() {
        System.out.println("Hello!");
    }
}
