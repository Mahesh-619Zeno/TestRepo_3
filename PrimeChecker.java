import java.util.Scanner;

public class PrimeChecker {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter a positive integer: ");
        int number = scanner.nextInt();

        String dbHost = System.getenv("DB_HOST");
        String dbPort = System.getenv("DB_PORT");
        String appSecret = System.getenv("APP_SECRET");

        if (dbHost == null || dbPort == null || appSecret == null) {
            System.out.println("Missing environment variables. Please set DB_HOST, DB_PORT, and APP_SECRET.");
            return;
        }

        System.out.println("Connecting to database at " + dbHost + ":" + dbPort);
        System.out.println("Using app secret: " + appSecret);
    }
}
