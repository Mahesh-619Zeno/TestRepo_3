import json
import os
from datetime import datetime

DATA_FILE = os.path.join(os.path.dirname(__file__), "../data/tasks_data.json")

class Task:
    def __init__(self, title, description="", priority="Medium", deadline=None):
        self.title = title
        self.description = description
        self.priority = priority
        self.status = "Pending"  # Default status
        # deadline as ISO format string, e.g., "2025-10-30 15:00"
        self.deadline = deadline  

    def is_overdue(self):
        if self.deadline and self.status.lower() != "completed":
            deadline_dt = datetime.strptime(self.deadline, "%Y-%m-%d %H:%M")
            return datetime.now() > deadline_dt
        return False

    def time_to_deadline(self):
        if self.deadline:
            deadline_dt = datetime.strptime(self.deadline, "%Y-%m-%d %H:%M")
            return (deadline_dt - datetime.now()).total_seconds()
        return None

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
            "Status": t.status,
            "Deadline": t.deadline
        } for t in self.tasks]

    def save_tasks(self):
        data = [t.__dict__ for t in self.tasks]
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=2)

    def load_tasks(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as f:
                data = json.load(f)
                self.tasks = [Task(**d) for d in data]

    def get_overdue_tasks(self):
        return [t for t in self.tasks if t.is_overdue()]

    def get_upcoming_deadline_tasks(self, within_seconds=86400):
        # Tasks with deadlines within the next 24 hours (86400 seconds)
        upcoming = []
        for t in self.tasks:
            time_left = t.time_to_deadline()
            if time_left is not None and 0 < time_left <= within_seconds and t.status.lower() != "completed":
                upcoming.append(t)
        return upcoming
