import java.util.Scanner;

public class PrimeChecker {

    // Method to check if a number is prime
    public static boolean isPrime(int num) {
        if (num <= 1) return false;         // 0 and 1 are not prime
        if (num == 2) return true;          // 2 is the only even prime number
        if (num % 2 == 0) return false;     // Eliminate other even numbers

        // Only check up to square root of num for efficiency
        for (int i = 3; i <= Math.sqrt(num); i += 2) {
            if (num % i == 0) return false;
        }

        return true;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        try {
            System.out.print("Enter a number to check if it's prime: ");
            int number = scanner.nextInt();

            if (isPrime(number)) {
                System.out.println(number + " is a prime number.");
            } else {
                System.out.println(number + " is not a prime number.");
            }

        } catch (Exception e) {
            System.out.println("Invalid input. Please enter an integer.");
        } finally {
            scanner.close();
        }
    }
}
