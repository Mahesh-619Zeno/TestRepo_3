import json
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "../data/users_tasks.json")

class Task:
    def __init__(self, title, description="", priority="Medium", category="General",
                 status="Pending", owner_id=None, shared_with=None):
        self.title = title
        self.description = description
        self.priority = priority
        self.category = category
        self.status = status
        self.owner_id = owner_id  # User ID who owns this task
        self.shared_with = shared_with if shared_with else []  # List of user IDs this task is shared with

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()

    def list_tasks(self, user_id=None, admin=False, filter_priority=None, filter_category=None):
        if admin:
            filtered_tasks = self.tasks
        else:
            filtered_tasks = [t for t in self.tasks if t.owner_id == user_id or user_id in t.shared_with]

        if filter_priority:
            filtered_tasks = [t for t in filtered_tasks if t.priority.lower() == filter_priority.lower()]
        if filter_category:
            filtered_tasks = [t for t in filtered_tasks if t.category.lower() == filter_category.lower()]

        priority_order = {"high": 1, "medium": 2, "low": 3}
        filtered_tasks.sort(key=lambda t: priority_order.get(t.priority.lower(), 4))

        return [{
            "Title": t.title,
            "Description": t.description,
            "Priority": t.priority,
            "Category": t.category,
            "Status": t.status,
            "OwnerID": t.owner_id,
            "SharedWith": t.shared_with
        } for t in filtered_tasks]

    def share_task(self, title, owner_id, share_with_user_id):
        for task in self.tasks:
            if task.title.lower() == title.lower() and task.owner_id == owner_id:
                if share_with_user_id not in task.shared_with and share_with_user_id != owner_id:
                    task.shared_with.append(share_with_user_id)
                    self.save_tasks()
                    return f"Task '{title}' shared successfully."
                else:
                    return f"Task '{title}' is already shared with this user or invalid user."
        return f"Task '{title}' not found or you do not own it."

    def save_tasks(self):
        data = {}
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as f:
                data = json.load(f)
        data["tasks"] = [t.__dict__ for t in self.tasks]
        data.setdefault("users", data.get("users", []))
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=2)

    def load_tasks(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as f:
                data = json.load(f)
                self.tasks = [Task(**t) for t in data.get("tasks", [])]
        else:
            self.tasks = []
