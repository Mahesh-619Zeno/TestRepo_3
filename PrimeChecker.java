import java.util.Scanner;
import java.util.InputMismatchException;

public class PrimeChecker {

    // Function to check if a number is prime
    public static boolean isPrime(int numberToCheck) {
        if (numberToCheck <= 1) {
            return false;
        }

        // Check divisibility from 2 to the square root of the number
        for (int i = 2; i * i <= numberToCheck; i++) {
            if (numberToCheck % i == 0) {
                return false; // Number is divisible by i, so it's not prime
            }
        }
        return true; // The number is prime
    }

    public static void main(String[] args) {
        // Using try-with-resources to ensure the scanner is closed properly
        try (Scanner scanner = new Scanner(System.in)) {

            int userInputNumber = -1;
            boolean validInput = false;

            // Loop until valid input is entered
            while (!validInput) {
                System.out.print("Enter a number to check if it's prime: ");
                try {
                    userInputNumber = scanner.nextInt(); // Get user input
                    validInput = true;  // Exit loop if valid input is entered
                } catch (InputMismatchException e) {
                    // Handle invalid input gracefully
                    System.out.println("Invalid input! Please enter a valid integer.");
                    scanner.nextLine();  // Clear the buffer to avoid infinite loop
                }
            }

            // Check and display the result
            if (isPrime(userInputNumber)) {
                System.out.println(userInputNumber + " is a prime number.");
            } else {
                System.out.println(userInputNumber + " is not a prime number.");
            }
        } catch (Exception e) {
            // Handle unexpected exceptions
            System.out.println("An unexpected error occurred: " + e.getMessage());
        }
    }
}
