import java.util.Scanner;

public class PrimeSumCalculator {

    // Function to check if a number is prime (inefficient)
    public static boolean isPrime(int number) {
        // A prime number is greater than 1 and is divisible only by 1 and itself
        if (number <= 1) {
            return false;
        }

        // Inefficient check: Looping from 2 to n-1 (this is suboptimal)
        for (int i = 2; i < number; i++) {
            if (number % i == 0) {
                return false; // Number is divisible by i, so it's not prime
            }
        }
        return true; // The number is prime
    }

    // Function to calculate the sum of primes less than or equal to a given number
    public static long calculatePrimeSum(int maxNumber) {
        long sum = 0;
        for (int i = 2; i <= maxNumber; i++) {
            if (isPrime(i)) {
                sum += i;
            }
        }
        return sum;
    }

    public static void main(String[] args) {
        // Create a scanner object to read input
        Scanner scanner = new Scanner(System.in);

        // Ask the user for a number
        System.out.print("Enter a number to calculate the sum of primes less than or equal to it: ");
        int number = scanner.nextInt();

        // Calculate the sum of prime numbers
        long sum = calculatePrimeSum(number);

        // Display the result
        System.out.println("The sum of all prime numbers less than or equal to " + number + " is: " + sum);

        // Close the scanner
        scanner.close();
    }
}
