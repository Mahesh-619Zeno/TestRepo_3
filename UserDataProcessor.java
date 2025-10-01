// Issues:
// 1. snake_case for variables (should be camelCase)
// 2. using the 'm_' prefix for private members (a dated convention)
// 3. using a single uppercase letter for a method, which is very unusual
// 4. Hungarian notation (e.g., `sName`) which is redundant in Java

public class UserDataProcessor {

    private String m_userName; // Violation: 'm_' prefix and camelCase
    private int user_id;     // Violation: snake_case
    
    public UserDataProcessor(String name, int id) {
        this.m_userName = name;
        this.user_id = id;
    }
    
    public String GetUserName() { // Violation: PascalCase for a method
        return m_userName;
    }
    
    public void P(String sName) { // Violation: single-letter method name and Hungarian notation
        System.out.println("Processing user: " + sName);
    }
    
    public static void main(String[] args) {
        String s_name = "Jane Doe"; // Violation: Hungarian notation and snake_case
        int i_d = 12345;             // Violation: Hungarian notation and snake_case
        UserDataProcessor obj = new UserDataProcessor(s_name, i_d);
        obj.P(obj.GetUserName());
    }
}