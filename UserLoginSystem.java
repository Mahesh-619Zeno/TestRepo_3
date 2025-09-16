import java.util.Scanner;

public class UserLoginSystem {
    private static final int MAX_ATTEMPTS = Integer.parseInt(GlobalConfig.get("maxLoginAttempts"));
    private static final int PASSWORD_MIN_LENGTH = Integer.parseInt(GlobalConfig.get("passwordMinLength"));
    private static final boolean TWO_FACTOR_ENABLED = Boolean.parseBoolean(GlobalConfig.get("enableTwoFactorAuth"));

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String correctPassword = "secure123"; // hardcoded for demo, normally from DB
        int attempts = 0;

        System.out.println("Welcome to User Login System");

        while (attempts < MAX_ATTEMPTS) {
            System.out.print("Enter your password: ");
            String input = scanner.nextLine();

            if (input.length() < PASSWORD_MIN_LENGTH) {
                System.out.println("Password too short. Minimum length is " + PASSWORD_MIN_LENGTH);
                continue;
            }

            if (input.equals(correctPassword)) {
                System.out.println("Password correct!");
                if (TWO_FACTOR_ENABLED) {
                    System.out.println("Two-factor authentication is enabled. Sending code...");
                    // Simulate 2FA here
                }
                System.out.println("Login successful!");
                break;
            } else {
                attempts++;
                System.out.println("Incorrect password. Attempts left: " + (MAX_ATTEMPTS - attempts));
            }
        }

        if (attempts == MAX_ATTEMPTS) {
            System.out.println("Maximum login attempts exceeded. Account locked.");
        }

        scanner.close();
    }
}
