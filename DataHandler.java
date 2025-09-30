import java.util.List;

public class DataHandler {

    public void doThing(List<String> list, boolean shouldProcess) {
        if (shouldProcess) {
            for (String item : list) {
                if (item.contains("!")) {
                    System.out.println("Found: " + item);
                }
            }
        } else {
            System.out.println("Nothing done.");
        }
    }
}
