import java.util.Scanner;

public class PrimeChecker {

    // Method to check if a number is prime
    public static boolean isPrime(int num) {
        if (num <= 1) return false;
        if (num == 2) return true;
        if (num % 2 == 0) return false;

        for (int i = 3; i <= Math.sqrt(num); i += 2) {
            if (num % i == 0) return false;
        }

        return true;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("=== " + GlobalConfig.get("appName") + " ===");

        try {
            System.out.print("Enter a number to check if it's prime: ");
            int number = scanner.nextInt();

            int maxAllowed = GlobalConfig.getInt("maxAllowedInput");
            boolean logging = GlobalConfig.getBoolean("enableLogging");

            if (number > maxAllowed) {
                System.out.println("Input exceeds maximum allowed value (" + maxAllowed + ").");
                return;
            }

            boolean result = isPrime(number);

            if (logging) {
                System.out.println("Checked number: " + number + ", Prime: " + result);
            } else {
                System.out.println(result ? "Prime number." : "Not a prime number.");
            }

        } catch (Exception e) {
            System.out.println("Invalid input. Please enter an integer.");
        } finally {
            scanner.close();
        }
    }
}
