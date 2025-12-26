from task.users import UserManager
from getpass import getpass

class AuthSystem:
    def __init__(self):
        self.user_manager = UserManager()
        self.current_user = None

    def login(self):
        while True:
            username = input("Username: ").strip()
            password = getpass("Password: ").strip()
            user = self.user_manager.find_by_username(username)
            if user and user.password == password:
                self.current_user = user
                print(f"Welcome, {user.username}! Role: {user.role}")
                return user
            print("Invalid credentials. Try again.")

    def logout(self):
        if self.current_user:
            print(f"Logging out {self.current_user.username}...")
            self.current_user = None
        print("You have been logged out.")

    def switch_user(self):
        self.logout()
        return self.login()