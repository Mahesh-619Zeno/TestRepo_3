# Issues:
# 1. mixedCase for variables and functions (should be snake_case)
# 2. overly short and non-descriptive variable names
# 3. mixing conventions (e.g., camelCase for a function and snake_case for a class method)
# 4. using a single uppercase letter for a constant, which is confusing
# 5. a useless variable name like 'temp' or 'tmp'

GLOBAL_MAX = 1000  # Confusing - single uppercase letter for a global variable
a_list = []

class UserProcessor:
    def __init__(self, some_info):
        self.someInfo = some_info
        self.tmp = "temporary data" # Useless variable name

    def fetchUserData(self): # Violation: camelCase for a function
        # A list to store processed user data.
        the_list = []
        for x in range(len(self.someInfo)): # Violation: 'x' is not descriptive
            user = self.someInfo[x]
            if user.is_active():
                the_list.append(user)
        return the_list

def process_and_save_data(userData): # Violation: camelCase argument name
    if len(userData) > GLOBAL_MAX:
        print("Data exceeds max limit")
        return

    processed_data = []
    for u in userData:
        processed_data.append(u.process())
    
    # Save the processed data
    file_writer = FileWriter()
    file_writer.Write(processed_data) # Violation: PascalCase for a method