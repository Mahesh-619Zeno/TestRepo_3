from task.task import Task, TaskManager
from task.status import update_status
from task.search import search_by_title
from task.deadline import set_deadline, remove_deadline, grant_extension
from task.scheduler import start_scheduler
from task.analytics import get_upcoming_deadlines
from datetime import datetime, timedelta, timezone

def notify(msg):
    print(f"[NOTIFICATION] {msg}")

def main():
    manager = TaskManager()
    print("=== Task Manager with Deadlines ===")

    # Add sample tasks
    manager.add_task(Task("Submit Report", "Weekly financial summary", "High"))
    manager.add_task(Task("Team Sync", "Weekly meeting", "Medium", is_recurring=True,
                          recurrence_pattern={"frequency": "weekly", "interval": 1}))

    # Set a deadline for a task
    future_dt = (datetime.now(timezone.utc) + timedelta(minutes=5)).isoformat()
    print(set_deadline(manager, "Submit Report", future_dt, reminder_minutes=2))

    # Start scheduler background thread
    start_scheduler(manager, notify)

    # Display all tasks
    print("\n--- All Tasks ---")
    for task in manager.list_tasks(sort_by_due_date=True):
        print(task)

    # Show upcoming deadline analytics
    print("\n--- Upcoming Deadlines ---")
    for entry in get_upcoming_deadlines(manager):
        print(entry)

if __name__ == "__main__":
    main()
