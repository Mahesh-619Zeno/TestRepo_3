import java.io.FileInputStream;
import java.io.IOException;
import java.util.Properties;

public class Config {
    // Global config variable for preferred temperature unit
    public static String preferredUnit = "C"; // default Celsius

    public static void loadConfig(String configFilePath) {
        Properties props = new Properties();
        try (FileInputStream fis = new FileInputStream(configFilePath)) {
            props.load(fis);
            String unit = props.getProperty("temperature.unit");
            if (unit != null && (unit.equalsIgnoreCase("C") || unit.equalsIgnoreCase("F"))) {
                preferredUnit = unit.toUpperCase();
            }
        } catch (IOException e) {
            System.out.println("Could not load config, using defaults.");
        }
    }
}
