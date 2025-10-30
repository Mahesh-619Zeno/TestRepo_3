from tasks.task_deadline import TaskWithDeadline, TaskManagerWithDeadline
from tasks.status import update_status
from tasks.search import search_by_title, search_by_priority

def main():
    manager = TaskManagerWithDeadline()
    print("=== Welcome to Task Manager with Deadlines ===")

    # Add tasks with deadlines and optional reminders
    manager.add_task(TaskWithDeadline("Finish Report", "Complete the financial report", "High", due_date="2025-10-20T17:00:00", reminder_time="2025-10-19T09:00:00"))
    manager.add_task(TaskWithDeadline("Email Client", "Send project updates", "Medium", due_date="2025-10-18T12:00:00"))
    manager.add_task(TaskWithDeadline("Team Meeting", "Discuss project roadmap", "Low"))

    print("\n--- All Tasks ---")
    for t in manager.list_tasks(sort_by_due_date=True):
        print(t)

    print("\n--- Overdue Tasks ---")
    overdue = manager.list_overdue_tasks()
    for t in overdue:
        print(t if isinstance(t, str) else vars(t))

    print("\n--- Upcoming Reminders ---")
    reminders = manager.list_upcoming_reminders(days=7)
    for t in reminders:
        print(t if isinstance(t, str) else vars(t))

    # Update status - integrate with your existing status update function
    print("\n--- Update Status ---")
    print(update_status(manager, "Finish Report", "In-Progress"))

    # Search functionality remains unchanged
    print("\n--- Search by Title 'Team' ---")
    results = search_by_title(manager, "Team")
    for t in results:
        print(vars(t))

if __name__ == "__main__":
    main()