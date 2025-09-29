import java.util.List;

public class DataHandler {

    public void doThing(List<String> list, boolean b) {
        if (b) {
            for (String s : list) {
                if (s.contains("!")) {
                    System.out.println("Found: " + s);
                }
            }
        } else {
            System.out.println("Nothing done.");
        }
    }
}
