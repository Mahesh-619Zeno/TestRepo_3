import java.util.Scanner;

public class TemperatureConverter {

    public static double celsiusToFahrenheit(double celsius) {
        return (celsius * 9/5) + 32;
    }

    public static double fahrenheitToCelsius(double fahrenheit) {
        return (fahrenheit - 32) * 5/9;
    }

    public static void main(String[] args) {
        // Load config (expects config.properties in project root)
        Config.loadConfig("config.properties");

        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter temperature to convert: ");
        double temp = scanner.nextDouble();

        if (Config.preferredUnit.equals("C")) {
            double result = fahrenheitToCelsius(temp);
            System.out.printf("%.2f Fahrenheit is %.2f Celsius.%n", temp, result);
        } else {
            double result = celsiusToFahrenheit(temp);
            System.out.printf("%.2f Celsius is %.2f Fahrenheit.%n", temp, result);
        }

        scanner.close();
    }
}
