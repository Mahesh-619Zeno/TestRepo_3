import datetime
import threading
import time

class DeadlineReminderManager:
    def __init__(self, task_manager):
        self.task_manager = task_manager
        self.running = False

    def validate_due_date(self, due_date_str):
        try:
            due_date = datetime.datetime.strptime(due_date_str, "%Y-%m-%dT%H:%M:%S")
            if due_date < datetime.datetime.utcnow():
                return False, "Due date must be in the future (UTC)."
            return True, due_date
        except ValueError:
            return False, "Invalid due date format. Use YYYY-MM-DDTHH:MM:SS."

    def set_deadline(self, title, due_date_str, reminder_minutes=None):
        valid, due_date_or_msg = self.validate_due_date(due_date_str)
        if not valid:
            return due_date_or_msg

        for task in self.task_manager.tasks:
            if task.title.lower() == title.lower():
                task.due_date = due_date_or_msg.isoformat()
                task.reminder_time = reminder_minutes
                self.task_manager.save_tasks()
                return f"Deadline set for task '{task.title}' with reminder {reminder_minutes} minutes before."
        return f"Task '{title}' not found."

    def remove_deadline(self, title):
        for task in self.task_manager.tasks:
            if task.title.lower() == title.lower():
                task.due_date = None
                task.reminder_time = None
                self.task_manager.save_tasks()
                return f"Deadline removed for task '{task.title}'."
        return f"Task '{title}' not found."

    def _send_notification(self, task, message):
        # Extend with email or UI alert integration
        print(f"NOTIFICATION: {message} (Task: {task.title})")

    def start_scheduler(self, interval_sec=60):
        if self.running:
            return
        self.running = True
        threading.Thread(target=self._scheduler_loop, args=(interval_sec,), daemon=True).start()

    def _scheduler_loop(self, interval_sec):
        while self.running:
            now = datetime.datetime.utcnow()
            updated = False
            for task in self.task_manager.tasks:
                if hasattr(task, 'due_date') and task.due_date:
                    due_date = datetime.datetime.fromisoformat(task.due_date)
                    # Update status if overdue
                    if due_date < now and task.status.lower() not in ['done', 'overdue']:
                        task.status = 'Overdue'
                        self._send_notification(task, f"Task is overdue since {due_date}")
                        updated = True
                    # Send reminder if reminder_time is set
                    elif task.reminder_time:
                        reminder_time = due_date - datetime.timedelta(minutes=task.reminder_time)
                        if reminder_time <= now < due_date:
                            self._send_notification(task, f"Reminder: Task '{task.title}' due at {due_date}")
            if updated:
                self.task_manager.save_tasks()
            time.sleep(interval_sec)

    def stop_scheduler(self):
        self.running = False