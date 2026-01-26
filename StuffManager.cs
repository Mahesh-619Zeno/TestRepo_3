// Issues:
// 1. snake_case for local variables and method parameters (should be camelCase)
// 2. PascalCase for a private field (should be camelCase)
// 3. Underscore prefix on a public property
// 4. a generic and vague name for a class
// 5. a generic name for a method

public class StuffManager
{
    private string Customer_Name; // Violation: PascalCase for a private field
    private readonly string Account_Number; // Violation: snake_case

    public StuffManager(string accNum)
    {
        Account_Number = accNum;
    }

    public void DoStuff(string user_name) // Violation: snake_case for method parameter
    {
        string customer_name = "Jane Smith"; // Violation: snake_case for local variable
        
        Customer_Name = customer_name;
        
        if (customer_name != null)
        {
            Console.WriteLine($"Processing data for {customer_name}");
        }
    }
}

public class MyProgram
{
    public static void Main()
    {
        StuffManager my_manager = new StuffManager("12345"); // Violation: snake_case for a variable
        my_manager.DoStuff("Jane Doe");
    }
}