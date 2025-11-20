import threading
import time
from datetime import datetime, timedelta
import pytz

class SchedulerService:
    def __init__(self, task_manager, notify_function):
        self.task_manager = task_manager
        self.notify = notify_function
        self.running = False

    def check_tasks(self):
        now = datetime.now(pytz.UTC)
        for task in self.task_manager.tasks:
            # Skip completed tasks
            if task.status.lower() == "done":
                continue
            
            # Update overdue status
            if task.due_date and task.status.lower() != "overdue":
                if task.due_date < now:
                    task.status = "Overdue"
                    self.task_manager.save_tasks()
                    self.notify(task, "overdue")

            # Check reminders
            if task.due_date and task.reminder_time:
                reminder_time = task.due_date - timedelta(minutes=task.reminder_time)
                if reminder_time <= now < task.due_date and task.status.lower() != "overdue":
                    self.notify(task, "reminder")

    def start(self, interval_seconds=60):
        self.running = True
        def run():
            while self.running:
                try:
                    self.check_tasks()
                except Exception as e:
                    print(f"Scheduler error: {e}")
                time.sleep(interval_seconds)
        threading.Thread(target=run, daemon=True).start()

    def stop(self):
        self.running = False

def example_notify(task, notification_type):
    if notification_type == "reminder":
        print(f"[Reminder] Task '{task.title}' is due soon at {task.due_date}.")
    elif notification_type == "overdue":
        print(f"[Overdue] Task '{task.title}' is past due! Due date was {task.due_date}.")