import java.util.Scanner;

public class BankingApp {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String appName = GlobalConfig.get("appName");
        int maxWithdrawal = GlobalConfig.getInt("maxWithdrawalLimit");
        boolean auditLogEnabled = GlobalConfig.getBoolean("enableAuditLog");

        System.out.println("Welcome to " + appName);
        System.out.println("Maximum withdrawal limit: $" + maxWithdrawal);

        try {
            System.out.print("Enter withdrawal amount: ");
            int amount = scanner.nextInt();

            if (amount > maxWithdrawal) {
                System.out.println("❌ Transaction denied. Amount exceeds limit of $" + maxWithdrawal);
            } else {
                System.out.println("✅ Withdrawal of $" + amount + " processed.");
                if (auditLogEnabled) {
                    System.out.println("[Audit] Withdrawal logged at " + System.currentTimeMillis());
                }
            }

        } catch (Exception e) {
            System.out.println("Invalid input. Please enter a valid number.");
        } finally {
            scanner.close();
        }

        System.out.println("For support, contact: " + GlobalConfig.get("supportEmail"));
    }
}
