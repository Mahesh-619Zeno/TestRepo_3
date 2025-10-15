import json
import os
from datetime import datetime, timedelta

DATA_FILE = os.path.join(os.path.dirname(__file__), "../data/tasks_deadlines.json")

class DeadlineTask:
    def __init__(self, title, description="", priority="Medium", due_date=None, due_time=None,
                 reminder_time=None, is_recurring=False, recurrence_pattern=None, assigned_user=None):
        self.title = title
        self.description = description
        self.priority = priority
        self.status = "To Do"  # Default status
        self.due_date = due_date           # "YYYY-MM-DD"
        self.due_time = due_time           # "HH:MM"
        self.reminder_time = reminder_time # minutes before due
        self.is_recurring = is_recurring
        self.recurrence_pattern = recurrence_pattern  # e.g., {"frequency": "daily", "interval": 1}
        self.assigned_user = assigned_user

    def due_datetime(self):
        if self.due_date and self.due_time:
            return datetime.strptime(f"{self.due_date} {self.due_time}", "%Y-%m-%d %H:%M")
        return None

    def to_dict(self):
        return self.__dict__

class DeadlineTaskManager:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def add_task(self, task: DeadlineTask):
        self.tasks.append(task)
        self.save_tasks()

    def list_tasks(self, sort_by_due=False):
        tasks_list = [t.to_dict() for t in self.tasks]
        if sort_by_due:
            tasks_list.sort(key=lambda x: (x['due_date'] or "9999-12-31", x['due_time'] or "23:59"))
        return tasks_list

    def save_tasks(self):
        data = [t.to_dict() for t in self.tasks]
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=2)

    def load_tasks(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as f:
                data = json.load(f)
                self.tasks = [DeadlineTask(**d) for d in data]

    def check_overdue(self):
        now = datetime.now()
        overdue_tasks = []
        for task in self.tasks:
            due = task.due_datetime()
            if due and task.status not in ["Done", "Overdue"]:
                if now > due:
                    task.status = "Overdue"
                    overdue_tasks.append(task)
        if overdue_tasks:
            self.save_tasks()
        return overdue_tasks

    def get_upcoming_reminders(self):
        now = datetime.now()
        reminders = []
        for task in self.tasks:
            due = task.due_datetime()
            if due and task.status not in ["Done", "Overdue"] and task.reminder_time:
                reminder_time = due - timedelta(minutes=int(task.reminder_time))
                if reminder_time <= now < due:
                    reminders.append(task)
        return reminders

    def update_recurring_tasks(self):
        """Update due_date for recurring tasks whose deadline has passed."""
        for task in self.tasks:
            due = task.due_datetime()
            if due and task.is_recurring and task.status in ["Done", "Overdue"]:
                freq = task.recurrence_pattern.get("frequency")
                interval = task.recurrence_pattern.get("interval", 1)
                if freq == "daily":
                    due += timedelta(days=interval)
                elif freq == "weekly":
                    due += timedelta(weeks=interval)
                elif freq == "monthly":
                    month = due.month + interval
                    year = due.year + (month - 1) // 12
                    month = (month - 1) % 12 + 1
                    due = due.replace(year=year, month=month)
                task.due_date = due.strftime("%Y-%m-%d")
                task.due_time = due.strftime("%H:%M")
                task.status = "To Do"
        self.save_tasks()
