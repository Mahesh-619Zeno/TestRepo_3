# tasks/task_deadline.py

import json
import os
from datetime import datetime, timedelta

DATA_FILE = os.path.join(os.path.dirname(__file__), "../data/tasks_data.json")

class TaskWithDeadline:
    def __init__(self, title, description="", priority="Medium", due_date=None, reminder_time=None):
        self.title = title
        self.description = description
        self.priority = priority
        self.status = "Pending"
        self.due_date = due_date  # ISO 8601 string or None
        self.reminder_time = reminder_time  # ISO 8601 string or None

    def is_overdue(self):
        if self.due_date:
            due_dt = datetime.fromisoformat(self.due_date)
            return datetime.now() > due_dt and self.status != "Completed"
        return False

    def needs_reminder(self):
        if self.reminder_time:
            reminder_dt = datetime.fromisoformat(self.reminder_time)
            now = datetime.now()
            return now <= reminder_dt <= now + timedelta(days=7)  # upcoming 7 days reminders
        return False


class TaskManagerWithDeadline:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()

    def edit_task_due_date(self, title, due_date=None, reminder_time=None):
        for task in self.tasks:
            if task.title.lower() == title.lower():
                if due_date:
                    # Validate date format
                    try:
                        datetime.fromisoformat(due_date)
                        task.due_date = due_date
                    except ValueError:
                        return "Invalid due_date format. Use ISO 8601."
                if reminder_time:
                    try:
                        datetime.fromisoformat(reminder_time)
                        task.reminder_time = reminder_time
                    except ValueError:
                        return "Invalid reminder_time format. Use ISO 8601."
                self.save_tasks()
                return f"Task '{task.title}' updated with due date and reminder."
        return f"Task '{title}' not found."

    def list_tasks(self, sort_by_due_date=False, ascending=True):
        tasks_data = [{
            "Title": t.title,
            "Description": t.description,
            "Priority": t.priority,
            "Status": "Overdue" if t.is_overdue() else t.status,
            "Due Date": t.due_date,
            "Reminder Time": t.reminder_time,
        } for t in self.tasks]

        if sort_by_due_date:
            tasks_data = sorted(tasks_data, key=lambda x: x["Due Date"] or "", reverse=not ascending)
        return tasks_data

    def list_overdue_tasks(self):
        overdue = [t for t in self.tasks if t.is_overdue()]
        if not overdue:
            return ["No overdue tasks found."]
        return overdue

    def list_upcoming_reminders(self, days=7):
        upcoming = [t for t in self.tasks if t.reminder_time and datetime.fromisoformat(t.reminder_time) <= datetime.now() + timedelta(days=days)]
        if not upcoming:
            return ["No upcoming reminders found."]
        return upcoming

    def save_tasks(self):
        data = [t.__dict__ for t in self.tasks]
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=2)

    def load_tasks(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as f:
                data = json.load(f)
                self.tasks = [TaskWithDeadline(**d) for d in data]
        else:
            self.tasks = []
