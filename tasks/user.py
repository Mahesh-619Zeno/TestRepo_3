import json
import os
import uuid
from getpass import getpass

DATA_FILE = os.path.join(os.path.dirname(__file__), "../data/users_data.json")

class User:
    def __init__(self, username, password, role="User", user_id=None):
        self.user_id = user_id or str(uuid.uuid4())
        self.username = username
        self.password = password  # Plaintext for demo; should be hashed in prod
        self.role = role

class UserManager:
    def __init__(self):
        self.users = []
        self.load_users()

    def load_users(self):
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, "r") as f:
                    data = json.load(f)
                    self.users = [User(**u) for u in data]
            except json.JSONDecodeError:
                print("Error: users_data.json is corrupted.")
                self.users = []
        else:
            # Create a default admin if file doesn't exist
            self.users = [User("admin", "admin123", "Admin")]
            self.save_users()

    def save_users(self):
        data = [u.__dict__ for u in self.users]
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=2)

    def find_by_username(self, username):
        return next((u for u in self.users if u.username.lower() == username.lower()), None)

    def add_user(self, username, password, role="User"):
        if self.find_by_username(username):
            return f"Error: Username '{username}' already exists."
        new_user = User(username, password, role)
        self.users.append(new_user)
        self.save_users()
        return f"User '{username}' ({role}) added successfully."

    def remove_user(self, username, current_user):
        user = self.find_by_username(username)
        if not user:
            return f"Error: User '{username}' not found."
        if user.username == current_user.username:
            return "Error: Cannot delete the currently logged-in user."
        if user.role == "Admin" and sum(u.role == "Admin" for u in self.users) == 1:
            return "Error: Cannot delete the last remaining Admin."
        self.users.remove(user)
        self.save_users()
        return f"User '{username}' removed successfully."

    def list_users(self):
        return [{"Username": u.username, "Role": u.role, "ID": u.user_id} for u in self.users]