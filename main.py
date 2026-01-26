from tasks.task import Task, TaskManager
from tasks.status import update_status
from tasks.search import search_by_title, search_by_priority
from tasks.deadline import add_or_update_due_date

def main():
    manager = TaskManager()
    print("=== Welcome to Task Manager ===")

    # Sample tasks
    manager.add_task(Task("Finish Report", "Complete financial report", "High", "2025-10-30T09:00:00"))
    manager.add_task(Task("Team Meeting", "Discuss roadmap", "Medium", "2025-11-02T09:00:00"))
    manager.add_task(Task("Grocery Shopping", "Buy essentials", "Low"))

    # Add or update due date
    print("\n--- Update Due Date ---")
    print(add_or_update_due_date(manager, "Grocery Shopping", "2025-11-05 15:00"))

    # Try adding invalid date
    print(add_or_update_due_date(manager, "Team Meeting", "2025/11/02 09:00"))  # invalid format

    # List all tasks sorted by due date
    print("\n--- Tasks Sorted by Due Date ---")
    for t in manager.list_tasks(sort_by_due_date=True):
        print(t)

    # Update task status
    print("\n--- Update Status ---")
    print(update_status(manager, "Finish Report", "In-Progress"))

if __name__ == "__main__":
    main()