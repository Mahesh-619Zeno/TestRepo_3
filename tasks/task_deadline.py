from tasks.task_deadline import TaskWithDeadline, TaskManagerWithDeadline
from tasks.status import update_status
from tasks.search import search_by_title, search_by_priority

def list_overdue_command(manager):
    overdue_tasks = manager.list_overdue_tasks()
    print("\n--- Overdue Tasks ---")
    for t in overdue_tasks:
        if isinstance(t, str):
            print(t)  # Message e.g. "No overdue tasks found."
        else:
            # Print selected task info
            print(vars(t))

def view_reminders_command(manager, days=7):
    reminders = manager.list_upcoming_reminders(days=days)
    print(f"\n--- Upcoming Reminders (Next {days} days) ---")
    for t in reminders:
        if isinstance(t, str):
            print(t)  # Message like "No upcoming reminders found."
        else:
            print(vars(t))

def main():
    manager = TaskManagerWithDeadline()
    print("=== Welcome to Task Manager with Deadlines ===")

    # Add sample tasks with deadlines and optional reminders
    manager.add_task(TaskWithDeadline("Finish Report", "Complete the financial report", "High", due_date="2025-10-20T17:00:00", reminder_time="2025-10-19T09:00:00"))
    manager.add_task(TaskWithDeadline("Email Client", "Send project updates", "Medium", due_date="2025-10-18T12:00:00"))
    manager.add_task(TaskWithDeadline("Team Meeting", "Discuss project roadmap", "Low"))

    print("\n--- All Tasks ---")
    for t in manager.list_tasks(sort_by_due_date=True):
        print(t)

    # Update status example
    print("\n--- Update Status ---")
    print(update_status(manager, "Finish Report", "In-Progress"))

    # Search by title example
    print("\n--- Search by Title 'Team' ---")
    results = search_by_title(manager, "Team")
    for t in results:
        print(vars(t))

    # List overdue tasks command
    list_overdue_command(manager)

    # View reminders command (default upcoming 7 days)
    view_reminders_command(manager)

if __name__ == "__main__":
    main()
