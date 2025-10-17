import json
import os
from datetime import datetime, timedelta, timezone

DATA_FILE = os.path.join(os.path.dirname(__file__), "../data/tasks_data.json")

class Task:
    def __init__(self, title, description="", priority="Medium", due_date=None,
                 reminder_time=None, is_recurring=False, recurrence_pattern=None,
                 status="Pending", extended_due_dates=None):
        self.title = title
        self.description = description
        self.priority = priority
        self.status = status
        self.due_date = self._parse_datetime(due_date)
        self.reminder_time = reminder_time  # minutes before due_date
        self.is_recurring = is_recurring
        self.recurrence_pattern = recurrence_pattern
        self.extended_due_dates = extended_due_dates or {}  # user-specific extensions

    def _parse_datetime(self, value):
        if isinstance(value, str):
            try:
                return datetime.fromisoformat(value)
            except ValueError:
                return None
        return value

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "status": self.status,
            "due_date": self.due_date.isoformat() if self.due_date else None,
            "reminder_time": self.reminder_time,
            "is_recurring": self.is_recurring,
            "recurrence_pattern": self.recurrence_pattern,
            "extended_due_dates": self.extended_due_dates,
        }

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()

    def update_task(self, title, **kwargs):
        for t in self.tasks:
            if t.title.lower() == title.lower():
                for k, v in kwargs.items():
                    if hasattr(t, k):
                        setattr(t, k, v)
                self.save_tasks()
                return f"Task '{title}' updated successfully."
        return f"Task '{title}' not found."

    def list_tasks(self, sort_by_due_date=False, descending=False):
        tasks_list = [t.to_dict() for t in self.tasks]
        if sort_by_due_date:
            tasks_list.sort(key=lambda x: x["due_date"] or "", reverse=descending)
        return tasks_list

    def load_tasks(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as f:
                data = json.load(f)
                self.tasks = [Task(**d) for d in data]

    def save_tasks(self):
        data = [t.to_dict() for t in self.tasks]
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=2)
