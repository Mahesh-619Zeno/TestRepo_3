import java.io.FileInputStream;
import java.io.IOException;
import java.util.Properties;

public class Greeting {
    public static void main(String[] args) {
        Properties props = new Properties();

        try (FileInputStream fis = new FileInputStream("config.properties")) {
            props.load(fis);
            String greeting = props.getProperty("greeting");
            System.out.println(greeting);
        } catch (IOException e) {
            System.out.println("Error loading config: " + e.getMessage());
        }
    }
}
