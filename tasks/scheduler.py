import threading
import time
from datetime import datetime, timezone, timedelta

def check_reminders(task_manager, notify_callback):
    while True:
        now = datetime.now(timezone.utc)
        for t in task_manager.tasks:
            if not t.due_date:
                continue
            due_date = t.due_date if not isinstance(t.due_date, str) else datetime.fromisoformat(t.due_date)
            if t.status.lower() not in ["done", "overdue"]:
                # Reminder check
                if t.reminder_time:
                    reminder_time = due_date - timedelta(minutes=t.reminder_time)
                    if reminder_time <= now < due_date:
                        notify_callback(f"Reminder: Task '{t.title}' is due soon!")
                # Overdue check
                if now > due_date:
                    t.status = "Overdue"
                    notify_callback(f"Task '{t.title}' is now overdue!")
        task_manager.save_tasks()
        time.sleep(60)  # Check every minute

def start_scheduler(task_manager, notify_callback):
    thread = threading.Thread(target=check_reminders, args=(task_manager, notify_callback), daemon=True)
    thread.start()
