import json
import os
from datetime import datetime

DATA_FILE = os.path.join(os.path.dirname(__file__), "../data/tasks_data.json")

class Task:
    def __init__(self, title, description="", priority="Medium", due_date=None):
        self.title = title
        self.description = description
        self.priority = priority
        self.status = "Pending"
        self.due_date = due_date  # ISO 8601 string, e.g. "2025-10-25T18:30:00"

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "status": self.status,
            "due_date": self.due_date
        }

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()

    def get_task(self, title):
        for t in self.tasks:
            if t.title.lower() == title.lower():
                return t
        return None

    def list_tasks(self, sort_by_due_date=False):
        tasks_to_list = self.tasks
        if sort_by_due_date:
            def sort_key(t):
                if not t.due_date:
                    return datetime.max
                return datetime.fromisoformat(t.due_date)
            tasks_to_list = sorted(self.tasks, key=sort_key)
        return [t.to_dict() for t in tasks_to_list]

    def save_tasks(self):
        data = [t.to_dict() for t in self.tasks]
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=2)

    def load_tasks(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as f:
                data = json.load(f)
                self.tasks = [Task(**d) for d in data]