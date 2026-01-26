import time
from datetime import datetime
from tasks.task import TaskManager

def notify(task):
    print(f"REMINDER: Task '{task.title}' is due at {task.deadline} (Status: {task.status})")

def reminder_service(task_manager, check_interval=60):
    """
    Runs an ongoing reminder service that checks every check_interval seconds
    for upcoming or overdue tasks and notifies the user on console.
    """
    print("Starting reminder service...")
    while True:
        now = datetime.now()
        overdue_tasks = task_manager.get_overdue_tasks()
        upcoming_tasks = task_manager.get_upcoming_deadline_tasks(within_seconds=3600)  # 1 hour

        for task in overdue_tasks:
            notify(task)
        for task in upcoming_tasks:
            notify(task)

        time.sleep(check_interval)
