import time
from datetime import datetime, timedelta

def notify(task):
    print(f"NOTIFICATION: Task '{task.title}' is due by {task.deadline} (Status: {task.status})")

def reminder_service(task_manager, check_interval=60):
    """
    Continuously checks for overdue and upcoming tasks and sends notifications only once.
    It also updates task statuses as needed.
    """
    print("Starting reminder service...")
    while True:
        task_manager.update_overdue_statuses()

        # Remind overdue tasks
        for task in task_manager.get_overdue_tasks():
            if not task.reminder_sent:  # Notify only once
                notify(task)
                task.reminder_sent = True
                task_manager.save_tasks()

        # Remind upcoming tasks within next hour
        for task in task_manager.get_upcoming_deadline_tasks(within_seconds=3600):
            if not task.reminder_sent:
                notify(task)
                task.reminder_sent = True
                task_manager.save_tasks()

        time.sleep(check_interval)
