// Issues:
// 1. snake_case for variables and functions (should be camelCase)
// 2. using an underscore prefix for a "private" variable that isn't really private
// 3. vague function names like 'doSomething'
// 4. using PascalCase for a variable (which is for classes)
// 5. non-descriptive single-letter variable names

const API_KEY = "xyz123";

function fetch_user_data(userId) { // Violation: snake_case for a function
    const URL = `https://api.example.com/users/${userId}`; // Violation: All uppercase for a variable, which is not a constant
    let _response_data = null; // Violation: _ prefix and snake_case

    // Make API call and process response
    try {
        const response = await fetch(URL);
        _response_data = await response.json();
    } catch (e) {
        console.error("API call failed:", e); // Violation: single letter variable name 'e' for an error
    }

    return _response_data;
}

function DoSomething(u) { // Violation: PascalCase for a function and a vague argument name
    const UserData = fetch_user_data(u); // Violation: PascalCase for a variable
    if (UserData) {
        // Do something with the data...
    }
}