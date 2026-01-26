import java.io.InputStream;
import java.util.Properties;

public class AppConfig {
    private Properties properties = new Properties();

    public AppConfig() {
        try (InputStream input = getClass().getClassLoader().getResourceAsStream("config.properties")) {
            if (input == null) {
                System.out.println("Sorry, unable to find config.properties");
                return;
            }
            // Load properties file
            properties.load(input);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public String getAppName() {
        return properties.getProperty("app.name");
    }

    public String getAppVersion() {
        return properties.getProperty("app.version");
    }

    public String getLoggingLevel() {
        return properties.getProperty("logging.level");
    }

    public static void main(String[] args) {
        AppConfig config = new AppConfig();
        System.out.println("App Name: " + config.getAppName());
        System.out.println("App Version: " + config.getAppVersion());
        System.out.println("Logging Level: " + config.getLoggingLevel());
    }
}
