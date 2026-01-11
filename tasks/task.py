import json
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "../data/tasks_data.json")

class Task:
    def __init__(self, title, description="", priority="Medium"):
        self.title = title
        self.description = description
        self.priority = priority
        self.status = "Pending"

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()

    def list_tasks(self):
        return [{
            "Title": t.title,
            "Description": t.description,
            "Priority": t.priority,
            "Status": t.status
        } for t in self.tasks]

    def save_tasks(self):
        data = [t.__dict__ for t in self.tasks]
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=2)

    def load_tasks(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as f:
                try:
                    data = json.load(f)
                    self.tasks = [Task(**d) for d in data]
                except json.JSONDecodeError:
                    self.tasks = []

    def delete_task(self, title):
        """
        Deletes all tasks whose title matches (case-insensitive) the given 'title'.
        Returns True if at least one task was deleted, False otherwise.
        """
        if not isinstance(title, str) or not title.strip():
            return False

        original_count = len(self.tasks)
        self.tasks = [t for t in self.tasks if t.title.lower() != title.lower()]
        new_count = len(self.tasks)

        if new_count < original_count:
            self.save_tasks()
            return True
        return False