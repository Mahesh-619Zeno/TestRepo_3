import json
import os
from datetime import datetime, timedelta

DATA_FILE = os.path.join(os.path.dirname(__file__), "../data/tasks_deadlines.json")

class DeadlineTask:
    def __init__(self, title, description="", priority="Medium", due_date=None, reminder_time=None, recurring=None):
        self.title = title
        self.description = description
        self.priority = priority
        self.status = "Pending"
        self.due_date = due_date            # YYYY-MM-DD
        self.reminder_time = reminder_time  # HH:MM
        self.recurring = recurring          # 'daily', 'weekly', 'monthly'

    def to_dict(self):
        return self.__dict__

class DeadlineTaskManager:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def add_task(self, task: DeadlineTask):
        self.tasks.append(task)
        self.save_tasks()

    def list_tasks(self):
        return [t.to_dict() for t in self.tasks]

    def save_tasks(self):
        data = [t.to_dict() for t in self.tasks]
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=2)

    def load_tasks(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as f:
                data = json.load(f)
                self.tasks = [DeadlineTask(**d) for d in data]

    def get_overdue_tasks(self):
        overdue = []
        now = datetime.now()
        for task in self.tasks:
            if task.due_date and task.status != "Completed":
                due = datetime.strptime(task.due_date, "%Y-%m-%d")
                if due < now:
                    overdue.append(task)
                    if task.recurring:
                        self._update_recurring(task)
        return overdue

    def _update_recurring(self, task):
        due = datetime.strptime(task.due_date, "%Y-%m-%d")
        if task.recurring == "daily":
            due += timedelta(days=1)
        elif task.recurring == "weekly":
            due += timedelta(weeks=1)
        elif task.recurring == "monthly":
            month = due.month + 1
            year = due.year + (month - 1) // 12
            month = (month - 1) % 12 + 1
            due = due.replace(year=year, month=month)
        task.due_date = due.strftime("%Y-%m-%d")

    def check_reminders(self):
        now = datetime.now().strftime("%H:%M")
        reminders = [t for t in self.tasks if t.reminder_time == now and t.status != "Completed"]
        return reminders
