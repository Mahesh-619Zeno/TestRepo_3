from tasks.task import Task, TaskManager
from tasks.status import update_status
from tasks.search import search_by_title, search_by_priority
from tasks.delete import delete_task

def main():
    manager = TaskManager()
    print("=== Welcome to Task Manager ===")

    # Add sample tasks
    manager.add_task(Task("Finish Report", "Complete the financial report", "High"))
    manager.add_task(Task("Email Client", "Send project updates", "Medium"))
    manager.add_task(Task("Team Meeting", "Discuss project roadmap", "Low"))

    # List all tasks
    print("\n--- All Tasks ---")
    for t in manager.list_tasks():
        print(t)

    # Update status
    print("\n--- Update Status ---")
    print(update_status(manager, "Finish Report", "In-Progress"))

    # Delete a task
    print("\n--- Delete Task ---")
    print(delete_task(manager, "Email Client"))

    # List tasks after deletion
    print("\n--- Tasks After Deletion ---")
    for t in manager.list_tasks():
        print(t)

if __name__ == "__main__":
    main()
