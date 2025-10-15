import json
import os
from datetime import datetime, timedelta

DATA_FILE = os.path.join(os.path.dirname(__file__), "../data/tasks_data.json")

class Task:
    def __init__(self, title, description="", priority="Medium", deadline=None, status="Pending", reminder_sent=False):
        self.title = title
        self.description = description
        self.priority = priority
        self.status = status  # can be Pending, In-Progress, Completed, Overdue
        self.deadline = deadline  # string "YYYY-MM-DD HH:MM"
        self.reminder_sent = reminder_sent  # to track if reminder notification sent

    def is_overdue(self):
        if self.deadline and self.status.lower() not in ("completed", "overdue"):
            deadline_dt = datetime.strptime(self.deadline, "%Y-%m-%d %H:%M")
            if datetime.now() > deadline_dt:
                self.status = "Overdue"
                return True
        return False

    def time_to_deadline(self):
        if self.deadline:
            deadline_datetime = datetime.strptime(self.deadline, "%Y-%m-%d %H:%M")
            delta = deadline_dt - datetime.now()
            return delta.total_seconds()
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

    def update_overdue_statuses(self):
        updated = False
        for task in self.tasks:
            if task.is_overdue():
                updated = True
        if updated:
            self.save_tasks()

    def get_overdue_tasks(self):
        return [t for t in self.tasks if t.status.lower() == "overdue"]

    def get_upcoming_deadline_tasks(self, within_seconds=86400):
        upcoming = []
        for t in self.tasks:
            time_left = t.time_to_deadline()
            if time_left is not None and 0 < time_left <= within_seconds and t.status.lower() not in ("completed", "overdue"):
                upcoming.append(t)
        return upcoming

    def get_dashboard_summary(self):
        # Aggregation data for dashboard visualization
        summary = {
            "Total Tasks": len(self.tasks),
            "Completed": len([t for t in self.tasks if t.status.lower() == "completed"]),
            "Overdue": len([t for t in self.tasks if t.status.lower() == "overdue"]),
            "Pending": len([t for t in self.tasks if t.status.lower() == "pending"]),
            "In-Progress": len([t for t in self.tasks if t.status.lower() == "in-progress"])
        }
        return summary
