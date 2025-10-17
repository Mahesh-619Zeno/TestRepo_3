# tasks/task.py

import json
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "../data/tasks_data.json")

VALID_PRIORITIES = ["Low", "Medium", "High"]

class Task:
    def __init__(self, title, description="", priority="Medium", category="General"):
        if priority.capitalize() not in VALID_PRIORITIES:
            raise ValueError(f"Invalid priority '{priority}'. Valid options: {', '.join(VALID_PRIORITIES)}")
        if not category.strip():
            raise ValueError("Category cannot be empty.")
        self.title = title
        self.description = description
        self.priority = priority.capitalize()
        self.category = category.capitalize()
        self.status = "Pending"

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()

    def list_tasks(self):
        if not self.tasks:
            return "No tasks available."
        return [{
            "Title": t.title,
            "Description": t.description,
            "Priority": t.priority,
            "Category": t.category,
            "Status": t.status
        } for t in self.tasks]

    def save_tasks(self):
        data = [t.__dict__ for t in self.tasks]
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=2)

    def load_tasks(self):
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, "r") as f:
                    data = json.load(f)
                    self.tasks = [Task(**d) for d in data]
            except (json.JSONDecodeError, TypeError):
                print("Error: Failed to read tasks_data.json. File may be corrupted.")
                self.tasks = []
