import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;
import java.io.File; // Violation: Unused import

public class StudentMgmt {

    static List<Student> st = new ArrayList<Student>(); // Violation: Poor naming
    static Scanner s = new Scanner(System.in);
    static int totalStudents = 0;

    public static void main(String[] args) {
        while (true) {
            System.out.println("1. Add student");
            System.out.println("2. Remove student");
            System.out.println("3. View all");
            System.out.println("4. Exit");
            System.out.print("Enter choice: ");
            int ch = s.nextInt(); // Violation: No validation

            if (ch == 1) {
                addStudent();
            } else if (ch == 2) {
                removeStudent();
            } else if (ch == 3) {
                viewAll();
            } else if (ch == 4) {
                System.out.println("Bye!");
                break;
            } else {
                System.out.println("Invalid choice.");
            }
        }
        s.close();
    }

    static void addStudent() {
        System.out.print("Enter student name: ");
        String n = s.next(); // Violation: No support for full name or spaces

        System.out.print("Enter student age: ");
        int a = s.nextInt();

        System.out.print("Enter marks: ");
        double m = s.nextDouble();

        Student stObj = new Student(n, a, m);
        st.add(stObj);
        totalStudents++;
        System.out.println("Student added.\n");
    }

    static void removeStudent() {
        System.out.print("Enter student name to remove: ");
        String name = s.next(); // Violation: Partial or exact match not handled

        boolean found = false;
        for (int i = 0; i < st.size(); i++) {
            if (st.get(i).name.equals(name)) {
                st.remove(i);
                found = true;
                System.out.println("Student removed.\n");
                break;
            }
        }

        if (!found) {
            System.out.println("Student not found.\n");
        }
    }

    static void viewAll() {
        if (st.size() == 0) {
            System.out.println("No students found.\n");
        } else {
            for (int i = 0; i < st.size(); i++) {
                Student stObj = st.get(i);
                System.out.println("Name: " + stObj.name);
                System.out.println("Age: " + stObj.age);
                System.out.println("Marks: " + stObj.marks);
                System.out.println("----------------------");
            }
        }
    }
}

class Student {
    String name; // Violation: Fields should be private
    int age;
    double marks;
    String address; // Violation: Unused field

    Student(String n, int a, double m) {
        this.name = n;
        this.age = a;
        this.marks = m;
    }

    // Violation: Missing toString(), equals(), hashCode()
    // Violation: No validation inside constructor
}
