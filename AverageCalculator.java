import java.util.Scanner;

public class AverageCalculator {

    public static void main(String args[]) { // Violation 1: Missing `String[]` formatting (args[])
        Scanner input = new Scanner(System.in);
        int[] numbers = new int[5];
        int sum = 0;
        double average;

        System.out.println("Enter 5 numbers:");

        int i = 0;
        while (i < 5) {
            System.out.print("Number " + (i + 1) + ": ");
            if (input.hasNextInt()) {
                numbers[i] = input.nextInt();
                sum += numbers[i];
                i++;
            } else {
                System.out.println("Invalid input. Please enter an integer.");
                input.next();
            }
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
