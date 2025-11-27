import threading
import time
from datetime import datetime, timezone
from tasks.task import TaskManager

class NotificationService:
    def __init__(self, task_manager, user_manager, user_preferences):
        """
        task_manager: TaskManager
        user_manager: UserManager
        user_preferences: dict {user_id: {'email': bool, 'in_app': bool}}
        """
        self.task_manager = task_manager
        self.user_manager = user_manager
        self.user_preferences = user_preferences
        self._stop_event = threading.Event()

    def start(self, interval_seconds=60):
        def run():
            while not self._stop_event.is_set():
                try:
                    self.check_and_notify()
                except Exception as e:
                    print(f"Notification error: {e}")
                time.sleep(interval_seconds)
        self.thread = threading.Thread(target=run, daemon=True)
        self.thread.start()

    def stop(self):
        self._stop_event.set()
        if self.thread.is_alive():
            self.thread.join()

    def check_and_notify(self):
        now = datetime.utcnow().replace(tzinfo=timezone.utc)
        for task in self.task_manager.tasks:
            if task.status in ["Done"]:
                continue
            due_dt = task.get_due_datetime(task.user_manager.current_user.user_id if hasattr(self.task_manager, 'current_user') else None)
            reminder_dt = task.get_reminder_datetime()
            if reminder_dt and reminder_dt <= now < due_dt and task.status != "Overdue":
                self.notify_user(task, "reminder")
            if due_dt and now > due_dt and task.status != "Overdue" and task.status != "Done":
                task.status = "Overdue"
                self.notify_user(task, "overdue")
                self.task_manager.save_tasks()

    def notify_user(self, task, notification_type):
        user = next((u for u in self.user_manager.users if u.user_id == task.user_id), None)
        if not user:
            return
        msg = ""
        if notification_type == "reminder":
            msg = f"Reminder: Task '{task.title}' is due soon at {task.due_date} UTC for user {user.username}."
        elif notification_type == "overdue":
            msg = f"Alert: Task '{task.title}' is overdue since {task.due_date} UTC for user {user.username}."
        print(msg)
        # Integration for email/in-app notification based on user_preferences can be added here
