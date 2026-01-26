import json
import os
import uuid

DATA_FILE = os.path.join(os.path.dirname(__file__), "../data/users_tasks.json")

class User:
    def __init__(self, user_id, username, role="User"):
        self.user_id = user_id
        self.username = username
        self.role = role
        # Removed extra profile attributes here (e.g., email, phone)

class UserManager:
    def __init__(self):
        self.users = []
        self.load_users()
        # Removed session/login token management, outside this scope.

    def add_user(self, username, role="User"):
        if self.get_user_by_username(username):
            raise ValueError(f"User '{username}' already exists.")
        new_id = str(uuid.uuid4())
        user = User(new_id, username, role)
        self.users.append(user)
        self.save_users()
        return user

    def get_user_by_username(self, username):
        return next((u for u in self.users if u.username.lower() == username.lower()), None)

    def get_user_by_id(self, user_id):
        return next((u for u in self.users if u.user_id == user_id), None)

    def list_users(self):
        return [(u.user_id, u.username, u.role) for u in self.users]

    def delete_user(self, username):
        user = self.get_user_by_username(username)
        if user:
            self.users.remove(user)
            self.save_users()
            return True
        return False

    def load_users(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as f:
                data = json.load(f)
                self.users = [User(**u) for u in data.get("users", [])]
        else:
            self.users = []

    def save_users(self):
        data = {}
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as f:
                data = json.load(f)
        data["users"] = [u.__dict__ for u in self.users]
        data.setdefault("tasks", data.get("tasks", []))
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=2)

    
