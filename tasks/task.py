import json
import os

# Path to the task data file
DATA_FILE = os.path.join(os.path.dirname(__file__), "../data/tasks_data.json")

class Task:
    def __init__(self, title, description="", priority="Medium"):
        self.title = title
        self.description = description
        self.priority = priority
        self.status = "Pending"  # Default status

    def __repr__(self):
        return f"Task(title={self.title}, priority={self.priority}, status={self.status})"

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
        try:
            os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
            data = [t.__dict__ for t in self.tasks]
            with open(DATA_FILE, "w") as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            print(f"Error saving tasks: {e}")

    def load_tasks(self):
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, "r") as f:
                    data = json.load(f)
                    self.tasks = [Task(**d) for d in data]
            except Exception as e:
                print(f"Error loading tasks: {e}")
                self.tasks = []
