import time
from tasks.task import TaskManager

def notify(task):
    print(f"NOTIFICATION: Task '{task.title}' deadline at {task.deadline} (Status: {task.status})")

def reminder_service(task_manager, interval=60):
    """
    Runs continuously in background. Sends notifications once per task,
    updates statuses automatically.
    """
    print("Reminder service started...")
    while True:
        task_manager.update_overdue_statuses()

        # Notify overdue tasks if not already notified
        for t in task_manager.get_overdue_tasks():
            if not t.reminder_sent:
                notify(t)
                t.reminder_sent = True
                task_manager.save_tasks()

        # Notify tasks approaching deadline within 1 hour if not notified
        for t in task_manager.get_upcoming_deadline_tasks(3600):
            if not t.reminder_sent:
                notify(t)
                t.reminder_sent = True
                task_manager.save_tasks()

        time.sleep(interval)
