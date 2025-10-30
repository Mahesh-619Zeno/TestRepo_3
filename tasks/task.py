import json
import os
from tasks.priority_category import validate_priority, validate_category

DATA_FILE = os.path.join(os.path.dirname(__file__), "../data/tasks_data.json")

class Task:
    def __init__(self, title, description="", priority="Medium", category="General"):
        self.title = title
        self.description = description
        self.priority = validate_priority(priority)
        self.category = validate_category(category)
        self.status = "Pending"  # Default status

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()

    def list_tasks(self, filter_priority=None, filter_category=None, sort_by_priority=False):
        filtered = self.tasks
        from tasks.priority_category import filter_tasks_by_priority, filter_tasks_by_category, sort_tasks_by_priority

        if filter_priority:
            filtered = filter_tasks_by_priority(filtered, filter_priority)
        if filter_category:
            filtered = filter_tasks_by_category(filtered, filter_category)
        if sort_by_priority:
            filtered = sort_tasks_by_priority(filtered)

        return [{
            "Title": t.title,
            "Description": t.description,
            "Priority": t.priority,
            "Category": t.category,
            "Status": t.status
        } for t in filtered]

    def save_tasks(self):
        data = [t.__dict__ for t in self.tasks]
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=2)

    def load_tasks(self):
        if not os.path.exists(DATA_FILE):
            print(f"Warning: Data file '{DATA_FILE}' not found. Starting with empty task list.")
            self.tasks = []
            return
        try:
            with open(DATA_FILE, "r") as f:
                data = json.load(f)
                self.tasks = [Task(**d) for d in data]
        except json.JSONDecodeError:
            print(f"Error: Data file '{DATA_FILE}' is corrupted or contains invalid JSON. Starting with empty task list.")
            self.tasks = []
        except Exception as e:
            print(f"Unexpected error loading tasks: {e}. Starting with empty task list.")
            self.tasks = []